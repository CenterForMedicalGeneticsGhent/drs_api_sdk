# Checksums

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checksum** | **str** | The hex-string encoded checksum for the data | 
**type** | **str** | The digest method used to create the checksum. The         value (e.g. &#x60;&#x60;&#x60;sha-256&#x60;&#x60;&#x60;) SHOULD be listed as &#x60;&#x60;&#x60;Hash Name String&#x60;&#x60;&#x60; in the         https://www.iana.org/assignments/named-information/named-information.xhtml#hash-alg[IANA Named Information Hash Algorithm Registry].         Other values MAY be used, as long as implementors are aware of the issues         discussed in https://tools.ietf.org/html/rfc6920#section-9.4[RFC6920].         GA4GH may provide more explicit guidance for use of non-IANA-registered algorithms in the future.         Until then, if implementors do choose such an algorithm (e.g. because it&#x27;s implemented by their storage provider),         they SHOULD use an existing standard &#x60;&#x60;&#x60;type&#x60;&#x60;&#x60; value such as &#x60;&#x60;&#x60;md5&#x60;&#x60;&#x60;, &#x60;&#x60;&#x60;etag&#x60;&#x60;&#x60;, &#x60;&#x60;&#x60;crc32c&#x60;&#x60;&#x60;, &#x60;&#x60;&#x60;trunc512&#x60;&#x60;&#x60;, or &#x60;&#x60;&#x60;sha1&#x60;&#x60;&#x60;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

