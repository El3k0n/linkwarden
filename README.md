# LinkWarden API Wrapper
This is a simple Python wrapper for the LinkWarden API, it's still a work in progress, every contribution or suggestion is welcome!
I've had some difficulties understanding the parameters for some endpoints on the official [Linkwarden Api Documentation](https://docs.linkwarden.app/api/api-introduction), as they're not explained in big detail but often only through a name:type pair.

## Setup and Usage

For an (almost) complete guide on usage, take a look at [USAGE](USAGE.md)

## Implemented endpoints
- [x] Tags
- [x] Users
- [x] Collections
- [x] Avatar
- [x] Dashboard
- [x] Links
- [x] Logins
- [x] Migration
- [x] Public
- [x] Auth
- [x] Archives
- [x] Session
- [x] Search
- [x] Tokens 

## TODOs
- [ ] Check response formats in all the docstrings
- [ ] Adapt docstrings "Args" to the Google style
- [ ] Wrapper objects for links, collections, tags, users
- [x] Implement bulk update links
