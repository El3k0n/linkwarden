# LinkWarden API Wrapper
This is a simple Python wrapper for the LinkWarden API, it's still a work in progress, every contribution or suggestion is welcome!
I've had some difficulties understanding the parameters for some endpoints on the official [Linkwarden Api Documentation](https://docs.linkwarden.app/api/api-introduction), as they're not explained in big detail but often only through a name:type pair.

### Implemented endpoints
- [x] Tags
- [x] Users
- [x] Collections
- [x] Avatar
- [x] Dashboard
- [x] Links - Missing only bulk update
- [x] Logins
- [x] Migration
- [x] Public
- [ ] Auth
- [x] Archives
- [ ] Session
- [ ] Search
- [x] Tokens 

### TODOs
- [ ] Document response formats in each endpoint docstring
- [ ] Wrapper objects for links, collections, tags, users
- [ ] Implement bulk update links

### Usage

```python
from linkwarden import Api

# Initialize with your API key
api = Api("your-api-key-here")

#Or if you have a self-hosted instance
self_api = Api(api_key="your-api-key-here", base_url="http://linkwarden.yourdomain.com")

# Create a new link
new_link = api.links.create_link(
    name="My Link",
    url="https://example.com",
    type="url"
)

# Get collections
collections = api.collections.get_collections()

# Get tags
tags = api.tags.get_tags()

#Or get a tag by ID
tag = api.tags.get_tag(tag_id)

# Upload file to archive
api.archives.upload_file_to_archive(
    link_id=123,
    file_path="/path/to/file.pdf",
    format=2  # PDF
)
```