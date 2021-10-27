-- Функция для создания ALD-пользователей в Postgresql
CREATE OR REPLACE FUNCTION add_ald_users()
    RETURNS void AS
$$
DECLARE
    name text;
    arr  text[] := array [
        'mks',
        'mio',
        'mog',
        'mfo',
        'kraken',
        '"kraken-miv3-int"'
    ];
BEGIN
    FOREACH name IN ARRAY arr
        LOOP
            BEGIN
                EXECUTE format('CREATE USER %s', name);
                EXECUTE format('alter user %s set lo_compat_privileges = on', name);
                EXECUTE format('GRANT mks_service to %s', name);
            EXCEPTION
                WHEN DUPLICATE_OBJECT THEN
                    RAISE NOTICE 'not creating %', name;
            END;
        END LOOP;
END
$$ LANGUAGE plpgsql;


-- Функция для присвоения мандатных меток в Postgresql
CREATE OR REPLACE FUNCTION update_all_tables()
    RETURNS void AS
$$
DECLARE
    exist_tables CURSOR FOR
        SELECT table_name, table_schema
        FROM information_schema.tables
        WHERE table_schema NOT IN ('information_schema', 'pg_catalog');
    exist_schemas CURSOR FOR
        SELECT DISTINCT table_schema
        FROM information_schema.tables
        WHERE table_schema NOT IN ('information_schema', 'pg_catalog');
BEGIN
    MAC LABEL ON CLUSTER IS '{3,0}';
    MAC LABEL ON TABLESPACE pg_global IS '{3,0}';
    MAC CCR ON TABLESPACE pg_global IS OFF;
    MAC LABEL ON TABLESPACE pg_default IS '{3,0}';
    MAC CCR ON TABLESPACE pg_default IS OFF;
    MAC LABEL ON DATABASE mks IS '{3,0}';
    MAC CCR ON DATABASE mks IS OFF;

    FOR ex IN exist_schemas
        LOOP
            EXECUTE format('MAC LABEL ON SCHEMA %I IS ''{3,0}'' ', ex.table_schema);
            EXECUTE format('MAC CCR ON SCHEMA %I IS OFF', ex.table_schema);
        END LOOP;

    FOR ex IN exist_tables
        LOOP
            EXECUTE format('MAC LABEL ON TABLE %I.%I IS ''{3,0}'' ', ex.table_schema, ex.table_name);
            EXECUTE format('MAC CCR ON TABLE %I.%I IS OFF', ex.table_schema, ex.table_name);
            EXECUTE format('ALTER TABLE %I.%I SET WITH MACS', ex.table_schema, ex.table_name);
            EXECUTE format('CHMAC %I.%I SET maclabel = ''{0,0}'' WHERE maclabel = ''{3,0}''', ex.table_schema, ex.table_name);
        END LOOP;
END;
$$ LANGUAGE plpgsql;

do
$$
    begin
        perform add_ald_users();
        perform update_all_tables();
    end
$$;
