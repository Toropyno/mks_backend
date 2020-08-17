class FilestorageSerializer:

    def convert_object_to_json(self, filestorage):
        filestorage_dict = {
            'idFileStorage': filestorage.idfilestorage,
            'protocolFile': filestorage.filename,
            'protocols/download/' + filestorage.idfilestorage: filestorage.uri,
            'fileSize': filestorage.filesize,
            'mimeType': filestorage.mimeType,
            'createdOn': filestorage.createdOn,
            'description': filestorage.description,
            'authorId': filestorage.authorid}
        return filestorage_dict
