# coding: utf-8

"""
    Data Repository Service

     GET request:  - Fetch a DrsObject from the database by sending a unique ID through the request - Fetch an access url to the data which the object refers to - Fetch DrsObjects by doing a search on the aliases  POST request:  - Create a non-existing DrsObject in the database by giving an identifier  DELETE request:  - Delete a DrsObject from the database by unique identifier  PUT request:  - Update an existing DrsObject by unique identifier and the changes in the body   # noqa: E501

    OpenAPI spec version: 1.2.0
    Contact: ict@cmgg.be
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DrsObject(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'self_uri': 'str',
        'size': 'int',
        'created_time': 'str',
        'updated_time': 'str',
        'version': 'str',
        'mime_type': 'str',
        'checksums': 'AllOfDrsObjectChecksums',
        'access_methods': 'AllOfDrsObjectAccessMethods',
        'contents': 'AllOfDrsObjectContents',
        'description': 'str',
        'aliases': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'self_uri': 'self_uri',
        'size': 'size',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'version': 'version',
        'mime_type': 'mime_type',
        'checksums': 'checksums',
        'access_methods': 'access_methods',
        'contents': 'contents',
        'description': 'description',
        'aliases': 'aliases'
    }

    def __init__(self, id=None, name=None, self_uri=None, size=None, created_time=None, updated_time=None, version=None, mime_type=None, checksums=None, access_methods=None, contents=None, description=None, aliases=None):  # noqa: E501
        """DrsObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._self_uri = None
        self._size = None
        self._created_time = None
        self._updated_time = None
        self._version = None
        self._mime_type = None
        self._checksums = None
        self._access_methods = None
        self._contents = None
        self._description = None
        self._aliases = None
        self.discriminator = None
        self.id = id
        if name is not None:
            self.name = name
        self.self_uri = self_uri
        self.size = size
        self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if version is not None:
            self.version = version
        if mime_type is not None:
            self.mime_type = mime_type
        self.checksums = checksums
        if access_methods is not None:
            self.access_methods = access_methods
        if contents is not None:
            self.contents = contents
        if description is not None:
            self.description = description
        if aliases is not None:
            self.aliases = aliases

    @property
    def id(self):
        """Gets the id of this DrsObject.  # noqa: E501

        An identifier unique to this ```DrsObject```  # noqa: E501

        :return: The id of this DrsObject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DrsObject.

        An identifier unique to this ```DrsObject```  # noqa: E501

        :param id: The id of this DrsObject.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this DrsObject.  # noqa: E501

        A string that can be used to name a ```DrsObject```.         This string is made up of uppercase and lowercase letters, decimal digits, hypen, period, and underscore [A-Za-z0-9.-_].         See http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_282[portable filenames].  # noqa: E501

        :return: The name of this DrsObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DrsObject.

        A string that can be used to name a ```DrsObject```.         This string is made up of uppercase and lowercase letters, decimal digits, hypen, period, and underscore [A-Za-z0-9.-_].         See http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_282[portable filenames].  # noqa: E501

        :param name: The name of this DrsObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def self_uri(self):
        """Gets the self_uri of this DrsObject.  # noqa: E501

        A drs:// hostname-based URI, as defined in the DRS documentation, that tells clients how to access this object.         The intent of this field is to make DRS objects self-contained, and therefore easier for clients to store and pass around.         For example, if you arrive at this DRS JSON by resolving a compact identifier-based DRS URI,         the ```self_uri``` presents you with a hostname and properly encoded DRS ID for use in subsequent ```access``` endpoint calls.  # noqa: E501

        :return: The self_uri of this DrsObject.  # noqa: E501
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """Sets the self_uri of this DrsObject.

        A drs:// hostname-based URI, as defined in the DRS documentation, that tells clients how to access this object.         The intent of this field is to make DRS objects self-contained, and therefore easier for clients to store and pass around.         For example, if you arrive at this DRS JSON by resolving a compact identifier-based DRS URI,         the ```self_uri``` presents you with a hostname and properly encoded DRS ID for use in subsequent ```access``` endpoint calls.  # noqa: E501

        :param self_uri: The self_uri of this DrsObject.  # noqa: E501
        :type: str
        """
        if self_uri is None:
            raise ValueError("Invalid value for `self_uri`, must not be `None`")  # noqa: E501

        self._self_uri = self_uri

    @property
    def size(self):
        """Gets the size of this DrsObject.  # noqa: E501

        For blobs, the blob size in bytes. For bundles, the cumulative size, in bytes, of items in the contents field.  # noqa: E501

        :return: The size of this DrsObject.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DrsObject.

        For blobs, the blob size in bytes. For bundles, the cumulative size, in bytes, of items in the contents field.  # noqa: E501

        :param size: The size of this DrsObject.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def created_time(self):
        """Gets the created_time of this DrsObject.  # noqa: E501

        Timestamp of content creation in RFC3339. (This is the creation time of the underlying content, not of the JSON object.)  # noqa: E501

        :return: The created_time of this DrsObject.  # noqa: E501
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this DrsObject.

        Timestamp of content creation in RFC3339. (This is the creation time of the underlying content, not of the JSON object.)  # noqa: E501

        :param created_time: The created_time of this DrsObject.  # noqa: E501
        :type: str
        """
        if created_time is None:
            raise ValueError("Invalid value for `created_time`, must not be `None`")  # noqa: E501

        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this DrsObject.  # noqa: E501

        Timestamp of content update in RFC3339, identical to ```created_time``` in systems that do not support updates.         (This is the update time of the underlying content, not of the JSON object.)  # noqa: E501

        :return: The updated_time of this DrsObject.  # noqa: E501
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this DrsObject.

        Timestamp of content update in RFC3339, identical to ```created_time``` in systems that do not support updates.         (This is the update time of the underlying content, not of the JSON object.)  # noqa: E501

        :param updated_time: The updated_time of this DrsObject.  # noqa: E501
        :type: str
        """

        self._updated_time = updated_time

    @property
    def version(self):
        """Gets the version of this DrsObject.  # noqa: E501

        A string representing a version. (Some systems may use checksum, a RFC3339 timestamp, or an incrementing version number.)  # noqa: E501

        :return: The version of this DrsObject.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DrsObject.

        A string representing a version. (Some systems may use checksum, a RFC3339 timestamp, or an incrementing version number.)  # noqa: E501

        :param version: The version of this DrsObject.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def mime_type(self):
        """Gets the mime_type of this DrsObject.  # noqa: E501

        A string providing the mime-type of the ```DrsObject```.  # noqa: E501

        :return: The mime_type of this DrsObject.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this DrsObject.

        A string providing the mime-type of the ```DrsObject```.  # noqa: E501

        :param mime_type: The mime_type of this DrsObject.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

    @property
    def checksums(self):
        """Gets the checksums of this DrsObject.  # noqa: E501

        The checksum of the ```DrsObject```. At least one checksum must be provided.         For blobs, the checksum is computed over the bytes in the blob.         For bundles, the checksum is computed over a sorted concatenation of the checksums of its         top-level contained objects (not recursive, names not included).         The list of checksums is sorted alphabetically (hex-code) before concatenation         and a further checksum is performed on the concatenated checksum value.         For example, if a bundle contains blobs with the following checksums:         md5(blob1) = 72794b6d md5(blob2) = 5e089d29 Then the checksum of the bundle is:         md5( concat( sort( md5(blob1), md5(blob2) ) ) ) = md5( concat( sort( 72794b6d, 5e089d29 ) ) ) =         md5( concat( 5e089d29, 72794b6d ) ) = md5( 5e089d2972794b6d ) = f7a29a04  # noqa: E501

        :return: The checksums of this DrsObject.  # noqa: E501
        :rtype: AllOfDrsObjectChecksums
        """
        return self._checksums

    @checksums.setter
    def checksums(self, checksums):
        """Sets the checksums of this DrsObject.

        The checksum of the ```DrsObject```. At least one checksum must be provided.         For blobs, the checksum is computed over the bytes in the blob.         For bundles, the checksum is computed over a sorted concatenation of the checksums of its         top-level contained objects (not recursive, names not included).         The list of checksums is sorted alphabetically (hex-code) before concatenation         and a further checksum is performed on the concatenated checksum value.         For example, if a bundle contains blobs with the following checksums:         md5(blob1) = 72794b6d md5(blob2) = 5e089d29 Then the checksum of the bundle is:         md5( concat( sort( md5(blob1), md5(blob2) ) ) ) = md5( concat( sort( 72794b6d, 5e089d29 ) ) ) =         md5( concat( 5e089d29, 72794b6d ) ) = md5( 5e089d2972794b6d ) = f7a29a04  # noqa: E501

        :param checksums: The checksums of this DrsObject.  # noqa: E501
        :type: AllOfDrsObjectChecksums
        """
        if checksums is None:
            raise ValueError("Invalid value for `checksums`, must not be `None`")  # noqa: E501

        self._checksums = checksums

    @property
    def access_methods(self):
        """Gets the access_methods of this DrsObject.  # noqa: E501

        The list of access methods that can be used to fetch the ```DrsObject```. Required for single blobs; optional for bundles.  # noqa: E501

        :return: The access_methods of this DrsObject.  # noqa: E501
        :rtype: AllOfDrsObjectAccessMethods
        """
        return self._access_methods

    @access_methods.setter
    def access_methods(self, access_methods):
        """Sets the access_methods of this DrsObject.

        The list of access methods that can be used to fetch the ```DrsObject```. Required for single blobs; optional for bundles.  # noqa: E501

        :param access_methods: The access_methods of this DrsObject.  # noqa: E501
        :type: AllOfDrsObjectAccessMethods
        """

        self._access_methods = access_methods

    @property
    def contents(self):
        """Gets the contents of this DrsObject.  # noqa: E501

        If not set, this ```DrsObject``` is a single blob. If set, this ```DrsObject``` is a bundle containing         the listed ```ContentsObject``` s (some of which may be further nested).  # noqa: E501

        :return: The contents of this DrsObject.  # noqa: E501
        :rtype: AllOfDrsObjectContents
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this DrsObject.

        If not set, this ```DrsObject``` is a single blob. If set, this ```DrsObject``` is a bundle containing         the listed ```ContentsObject``` s (some of which may be further nested).  # noqa: E501

        :param contents: The contents of this DrsObject.  # noqa: E501
        :type: AllOfDrsObjectContents
        """

        self._contents = contents

    @property
    def description(self):
        """Gets the description of this DrsObject.  # noqa: E501

        A human readable description of the ```DrsObject```.  # noqa: E501

        :return: The description of this DrsObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DrsObject.

        A human readable description of the ```DrsObject```.  # noqa: E501

        :param description: The description of this DrsObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def aliases(self):
        """Gets the aliases of this DrsObject.  # noqa: E501

        A list of strings that can be used to find other metadata about this ```DrsObject``` from external metadata sources.         These aliases can be used to represent secondary accession numbers or external GUIDs.  # noqa: E501

        :return: The aliases of this DrsObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this DrsObject.

        A list of strings that can be used to find other metadata about this ```DrsObject``` from external metadata sources.         These aliases can be used to represent secondary accession numbers or external GUIDs.  # noqa: E501

        :param aliases: The aliases of this DrsObject.  # noqa: E501
        :type: list[str]
        """

        self._aliases = aliases

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DrsObject, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DrsObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other