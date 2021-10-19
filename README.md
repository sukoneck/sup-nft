# sup-nft
Scripts that query NFT metadata on various platforms. Currently there is only one and it's ***Just Fine™***

# artblocks-api

## how to use
Modify the top-level variables in the script: 
```
project_number = 37       # e.g. Paper Armada
project_feature = "Type"  # feature filter on or empty returns all features
project_value = "Swarm"   # the value of the feature you want 
starting_token = 0        # starts incrementing from here, used for testing
```
Then run it with `py ./artblocks-api`.

## how it works
Sends a request to the Art Blocks api for each token in the project and gathers the token feature/trait metadata. 

If the `project_feature` variable is empty (i.e. `""`), then all features are collected. When it's finished it spits out a map like: `{ "<token_id>": [ "<feature>": "<value>" ], ...}`

If the `project_feature` variable is populated (e.g. above), then only matching tokens are collected (e.g. `Type: Swarm`). When it's finished it spits out a list like: `[<token>, ...]`

## why it's barely usable
- Slow - Python takes a long time to slap out thousand(s) of requests.
- Wasteful - the Art Blocks api doesn't need to be dealing with this. 
- Redundant - want to run a few queries? that's a few thousand more unique requests.

## next steps, maybe
- Use the OpenSea API - Even without an API key, we can pull 50 at a time, rather than one.
- Re-write in Go - Hyperthread the slipstream for all those single-token api calls
- Cache it up - Slap the results into Mongo or something so that subsequent queries use the cache.  
- Existing tools - Use the official AB npm package https://github.com/ArtBlocks/node-artblocks 
