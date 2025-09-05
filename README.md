# LinkWarden API Wrapper
This is a simple Python wrapper for the LinkWarden API, it's still a work in progress, every contribution or suggestion is welcome!


## Installation

```bash
# Clone the repository
git clone https://github.com/El3k0n/linkwarden.git
cd linkwarden

# Install dependencies
pip install -r requirements.txt
```

## Configuration

### 1. Get API Key
1. Go to [Linkwarden](https://cloud.linkwarden.app)
2. Sign in to your account
3. Go to **Settings** → **API Keys**
4. Create a new API key
5. Copy the key

### 2. Initialize the wrapper
```python
from linkwarden import Api

#If using Linkwarden cloud
api = Api(api_key="your-api-key-here")

#If using a self-hosted instance

api = Api(
    api_key="your-api-key-here",
    base_url="http://linkwarden.yourdomain.com"
)

```

## Link Management

#### Get a specific link
```python
# Retrieve a link by ID
link = api.links.get_link(123)
print(f"Link: {link['name']}")
print(f"URL: {link['url']}")
print(f"Description: {link["description"]}")

# Get all links fields
link.keys()
```

#### Create a new link
```python
# Create a simple link
new_link = api.links.create_link(
    name="Google",
    url="https://google.com",
    type="url"
)
print(f"Link created with ID: {new_link['id']}")
print(f"Link created in collection: {new_link['collection']['id']} named {new_link['collection']['name']}")

# Create a link with tags and collection
new_link = api.links.create_link(
    name="Important Document",
    url="https://example.com/doc.pdf",
    type="pdf",
    description="Important work document",
    tags=[{"id": 1, "name": "work"}],
    collection={"id": 2, "name": "Work"}
)
```

#### Update a link
```python
# Update only some fields
updated_link = api.links.update_link(
    id=123, #Required
    name="New name", #Required
    url="http://example.com", #Required
    collection = { #All these collection fields are required
        "id":0,
        "name":"MyCollection",
        "ownerId":1
    }
    description="New description"
)
```

#### Archive a link
```python
# Archive a link
archived_link = api.links.archive_link(id=123)
print(archived_link)
```

#### Delete links
```python
# Delete a single link
api.links.delete_link(id=123)

# Delete multiple links
api.links.delete_link_list(ids=[123, 124, 125])
```

## User Management

#### Get all users
```python
users = api.users.get_users()
for user in users:
    print(f"ID: {user['id']}, Username: {user['username']}, Email: {user.get('email')}")
```

#### Get a specific user
```python
user = api.users.get_user(1)
print(f"User: {user['username']}")
```

#### Create a new user
```python
new_user = api.users.create_user(
    name="New User",
    password="password123",
    email="new@example.com",
    username="newuser"
)
```

#### Update a user
```python
updated_user = api.users.update_user(
    user_id=1,
    name="Updated Name",
    email="updated@example.com"
)
```

#### Delete a user
```python
api.users.delete_user(user_id=1)
```

## Tag Management

#### Get all tags
```python
tags = api.tags.get_tags()
for tag in tags:
    print(f"Tag: {tag['name']}, Color: {tag['color']}")
```

#### Get a specific tag
```python
tag = api.tags.get_tag(1)
print(f"Tag: {tag['name']}")
```

#### Update a tag
```python
updated_tag = api.tags.update_tag(
    tag_id=1,
    name="New Tag Name"
)
```

#### Delete a tag
```python
api.tags.delete_tag(tag_id=1)
```

## Collection Management

#### Get all collections
```python
collections = api.collections.get_collections()
for collection in collections:
    print(f"Collection: {collection['name']}")
```

#### Get a specific collection
```python
collection = api.collections.get_collection(1)
print(f"Collection: {collection['name']}")
```

#### Create a new collection
```python
new_collection = api.collections.create_collection(
    name="New Collection",
    description="Collection description"
)
```

#### Update a collection
```python
updated_collection = api.collections.update_collection(
    id=1,
    name="Updated Name"
)
```

#### Delete a collection
```python
api.collections.delete_collection(id=1)
```

## Dashboard

#### Get current user dashboard
```python
dashboard = api.dashboard.get_current_user_dashboard()
print(f"Got {len(dashboard)} entries")
print(f"First entry: {dashboard[0]["name"]}")
```

## Avatar Info

#### Get user avatar
```python
# Returns binary image data
avatar_bytes = api.avatar.get_avatar(1)

# Save to file
with open("avatar.png", "wb") as f:
    f.write(avatar_bytes)
```

## Search
```python
result = api.search.search_links(query="My Search")
result_links = result['data']['links']

print(f"Found {len(result_links)} results")
```

## API Token Management

#### Get all tokens
```python
tokens = api.tokens.get_tokens()
for token in tokens:
    print(f"Token: {token['name']}, Created: {token['createdAt']}")
```

#### Create a new token
```python
new_token = api.tokens.create_token(
    name="New Token",
    expires=1234567890  # Seconds to expire, 0 for never
)
print(f"Token created: {new_token['token']}")
```

#### Revoke a token
```python
api.tokens.revoke_token(token_id=1)
```

## Data Migration

#### Export data
```python
# Export all data
export_data = api.migration.export_data()
with open("export.json", "w") as f:
    f.write(export_data)
```

#### Import data
```python
# Import data from file
with open("export.json", "r") as f:
    data = f.read()

import_response = api.migration.import_data(data)
print(f"Response: {import_response}")
```

## Archive Management

#### Get PDF archive for link
```python
archive = api.archives.get_archive_by_link_id(link_id=123, format=2) #Get PDF archive
# Formats: 0 = PNG, 1 = JPEG, 2 = PDF, 3 = JSON, 4 = HTML

with open("archive.pdf", "wb") as f:
    f.write(archive)
```

#### Upload file to archive
```python
# From disk file
result = api.archives.upload_file_to_archive(
    link_id=123,
    file_path="/path/to/file.pdf",
    format="pdf"
)

# From file object
with open("file.pdf", "rb") as f:
    result = api.archives.upload_file_object_to_archive(
        link_id=123,
        file_object=f,
        format="pdf"
    )
```

## Public Endpoints

Public endpoints don't require authentication:

```python
# Get links from public collection
public_links = api.public.get_links_from_collection(collection_id=1)

# Get tags from public collection
public_tags = api.public.get_tags_from_collection(collection_id=1)

# Get public user
public_user = api.public.get_user_by_id(user_id=1)

# Get public link
public_link = api.public.get_link_by_id(link_id=1)

# Get public collection
public_collection = api.public.get_collection_by_id(collection_id=1)
```


## Additional Resources

- [Linkwarden API Documentation](https://docs.linkwarden.app/api)
- [GitHub Repository](https://github.com/El3k0n/linkwarden)
- [Issues and Bug Reports](https://github.com/El3k0n/linkwarden/issues)


