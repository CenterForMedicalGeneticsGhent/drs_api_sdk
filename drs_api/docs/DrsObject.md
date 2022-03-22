# DrsObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier unique to this &#x60;&#x60;&#x60;DrsObject&#x60;&#x60;&#x60; | 
**name** | **str** | A string that can be used to name a &#x60;&#x60;&#x60;DrsObject&#x60;&#x60;&#x60;.         This string is made up of uppercase and lowercase letters, decimal digits, hypen, period, and underscore [A-Za-z0-9.-_].         See http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_282[portable filenames]. | [optional] 
**self_uri** | **str** | A drs:// hostname-based URI, as defined in the DRS documentation, that tells clients how to access this object.         The intent of this field is to make DRS objects self-contained, and therefore easier for clients to store and pass around.         For example, if you arrive at this DRS JSON by resolving a compact identifier-based DRS URI,         the &#x60;&#x60;&#x60;self_uri&#x60;&#x60;&#x60; presents you with a hostname and properly encoded DRS ID for use in subsequent &#x60;&#x60;&#x60;access&#x60;&#x60;&#x60; endpoint calls. | 
**size** | **int** | For blobs, the blob size in bytes. For bundles, the cumulative size, in bytes, of items in the contents field. | 
**created_time** | **str** | Timestamp of content creation in RFC3339. (This is the creation time of the underlying content, not of the JSON object.) | 
**updated_time** | **str** | Timestamp of content update in RFC3339, identical to &#x60;&#x60;&#x60;created_time&#x60;&#x60;&#x60; in systems that do not support updates.         (This is the update time of the underlying content, not of the JSON object.) | [optional] 
**version** | **str** | A string representing a version. (Some systems may use checksum, a RFC3339 timestamp, or an incrementing version number.) | [optional] 
**mime_type** | **str** | A string providing the mime-type of the &#x60;&#x60;&#x60;DrsObject&#x60;&#x60;&#x60;. | [optional] 
**checksums** | **AllOfDrsObjectChecksums** | The checksum of the &#x60;&#x60;&#x60;DrsObject&#x60;&#x60;&#x60;. At least one checksum must be provided.         For blobs, the checksum is computed over the bytes in the blob.         For bundles, the checksum is computed over a sorted concatenation of the checksums of its         top-level contained objects (not recursive, names not included).         The list of checksums is sorted alphabetically (hex-code) before concatenation         and a further checksum is performed on the concatenated checksum value.         For example, if a bundle contains blobs with the following checksums:         md5(blob1) &#x3D; 72794b6d md5(blob2) &#x3D; 5e089d29 Then the checksum of the bundle is:         md5( concat( sort( md5(blob1), md5(blob2) ) ) ) &#x3D; md5( concat( sort( 72794b6d, 5e089d29 ) ) ) &#x3D;         md5( concat( 5e089d29, 72794b6d ) ) &#x3D; md5( 5e089d2972794b6d ) &#x3D; f7a29a04 | 
**access_methods** | **AllOfDrsObjectAccessMethods** | The list of access methods that can be used to fetch the &#x60;&#x60;&#x60;DrsObject&#x60;&#x60;&#x60;. Required for single blobs; optional for bundles. | [optional] 
**contents** | **AllOfDrsObjectContents** | If not set, this &#x60;&#x60;&#x60;DrsObject&#x60;&#x60;&#x60; is a single blob. If set, this &#x60;&#x60;&#x60;DrsObject&#x60;&#x60;&#x60; is a bundle containing         the listed &#x60;&#x60;&#x60;ContentsObject&#x60;&#x60;&#x60; s (some of which may be further nested). | [optional] 
**description** | **str** | A human readable description of the &#x60;&#x60;&#x60;DrsObject&#x60;&#x60;&#x60;. | [optional] 
**aliases** | **list[str]** | A list of strings that can be used to find other metadata about this &#x60;&#x60;&#x60;DrsObject&#x60;&#x60;&#x60; from external metadata sources.         These aliases can be used to represent secondary accession numbers or external GUIDs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

