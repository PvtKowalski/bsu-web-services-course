## Idea and API Outline

### Purpose

The idea behind this web-service is to allow pet-owners who lost their beloved pets to post ads, so that people who encounter suspected lost pets can make queries based on its properties, location of encounter, minimum reward, etc.

### Architectural style

"REST-like" is probably applicable term for this service, because:

1. WEB-service has a client-server architecture.
2. No client state is transferred during the client-server communication.
3. Cacheability.
4. Layered system.
4. Resources idenified in requests using URIs. The resources themselves are conceptually separate from the representations that are returned to the client.

But:

1. Client can hold a representation of `Pet` but can only delete it if he has a token, which is not contained in representation.
2. Messages are not quite self descriptive, because one needs to request a "schema" from `/animals/help` resource.

### Representations

#### Pet

```
{
	"id": unique identifier
	"species": dog/cat/parrot/...
	"breed": str
	"color": str, primary color
	"secondary_color": str or None, secondary color (spots or stripes)
	"name": str,
	"bounty": float $,
	"description": arbitrary string
	"traits": arbitrary string but with comma separated distinctive traits
	"image": bytes of small png image
	"latitude": float, approximate latitude
	"longitude": float, approximate longitude
	"owners_contacts": arbitrary string that describes how to contact the owner
}
```

### Resources

`/animals/` is a collection resource that represents all ads posted to the server

`/animals/search` represents a resource we use to make queries

To make a search an http GET request can be specified with parameters of:
- species of animal
- breed
- color
- secondary color
- separate words for traits search
- minimum bounty (to filter only caring owners)
- coordinates of encounter
- max radius of search (km)

E. g. `/animals/search?species=dog&color=black&seccolor=white&latitude=12.34&longitude=12.34&radius=100&minbounty=30`

`/animals/help` is a resource we can GET to recieve help (some "schema" of json? possible values for species, breed, color etc. fields?)

`animals/<token>` used by owners to delete ads

### API

#### To publish an ad about your lost pet

*POST* to `/animals/` with `Pet` representation payload.

Returns a unique token that can be used to delete your ad.

#### To search for ads that match some criteria

*GET* request to `/animals/search?params`

Returns a bunch or `Pet` jsons.

#### To delete an ad (to edit: DELETE + POST)

*DELETE* `/animals/<token>`

#### To get help

*GET* `/animals/help`
