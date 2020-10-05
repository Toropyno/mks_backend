from sqlalchemy import Column, Integer, VARCHAR

from mks_backend.models import Base


class LeadershipPosition(Base):
    """
    Перечень должностей руководства Министерства обороны РФ
    """
    __tablename__ = 'leadership_positions'

    leadership_positions_id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(40), unique=True, nullable=False)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)

    def __str__(self):
        return 'Должность id={id}, code={code}, fullname={fullname}'.format(
            id=self.leadership_positions_id,
            code=self.code,
            fullname=self.fullname
        )
