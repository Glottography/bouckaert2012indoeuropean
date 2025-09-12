# Releasing the dataset

## Recreate the raw data from glottography-data

```shell
cldfbench download cldfbench_bouckaert2012indoeuropean.py
```

## Recreate the CLDF data

```shell
cldfbench makecldf cldfbench_bouckaert2012indoeuropean.py --glottolog-version v5.2
cldfbench cldfreadme cldfbench_bouckaert2012indoeuropean.py
cldfbench zenodo cldfbench_bouckaert2012indoeuropean.py
cldfbench readme cldfbench_bouckaert2012indoeuropean.py
```

## Validation

```shell
cldf validate cldf
```

```shell
cldfbench geojson.validate cldf
```

```shell
cldfbench geojson.glottolog_distance cldf --format pipe
```

| ID | Distance | Contained | NPolys |
|:---------|-----------:|:------------|---------:|
| anci1242 | 2.17 | False | 1 |
| arom1237 | 0.08 | False | 1 |
| assa1263 | 0.00 | True | 1 |
| aves1237 | 0.00 | False | 1 |
| bela1254 | 0.00 | True | 1 |
| beng1280 | 0.00 | True | 1 |
| bret1244 | 0.00 | True | 1 |
| bulg1262 | 0.00 | True | 1 |
| cent1973 | 0.00 | True | 1 |
| chur1257 | 1.48 | False | 1 |
| corn1251 | 0.02 | False | 1 |
| czec1258 | 0.00 | True | 1 |
| dani1285 | 0.00 | True | 1 |
| digo1242 | 0.00 | True | 1 |
| faro1244 | 0.00 | True | 1 |
| friu1240 | 0.00 | True | 1 |
| goth1244 | 13.12 | False | 1 |
| guja1252 | 0.00 | True | 1 |
| hind1269 | 0.00 | True | 1 |
| hitt1242 | 0.00 | True | 1 |
| icel1247 | 0.00 | True | 1 |
| iris1253 | 0.00 | True | 1 |
| ital1282 | 0.00 | True | 1 |
| kash1277 | 0.00 | True | 1 |
| ladi1250 | 0.00 | True | 1 |
| lati1261 | 0.00 | True | 1 |
| latv1249 | 0.00 | True | 1 |
| lith1251 | 0.00 | True | 1 |
| luxe1241 | 0.00 | False | 2 |
| lyci1241 | 0.00 | True | 1 |
| mace1250 | 0.00 | True | 1 |
| mara1378 | 0.00 | True | 1 |
| marw1260 | 0.00 | True | 1 |
| mode1248 | 2.82 | False | 1 |
| nepa1254 | 0.93 | False | 1 |
| norw1258 | 0.00 | True | 2 |
| nucl1235 | 0.00 | True | 2 |
| occi1239 | 0.00 | True | 1 |
| oldn1244 | 23.94 | False | 1 |
| oldp1254 | 0.00 | True | 1 |
| oriy1255 | 3.00 | False | 2 |
| osca1245 | 0.00 | True | 1 |
| poli1260 | 0.00 | True | 1 |
| port1283 | 0.00 | True | 1 |
| prus1238 | 3.47 | False | 1 |
| roma1326 | 0.43 | False | 1 |
| roma1327 | 0.00 | True | 1 |
| russ1263 | 0.00 | True | 1 |
| sans1269 | 7.61 | False | 1 |
| scot1243 | 1.44 | False | 1 |
| sind1272 | 0.00 | False | 1 |
| sinh1246 | 0.00 | True | 1 |
| slov1268 | 0.00 | True | 1 |
| slov1269 | 0.00 | True | 1 |
| sout1528 | 0.00 | False | 1 |
| stan1288 | 0.00 | True | 1 |
| stan1289 | 0.00 | True | 1 |
| stan1290 | 0.00 | True | 1 |
| stan1293 | 0.00 | True | 1 |
| swed1254 | 0.00 | True | 1 |
| taji1245 | 0.00 | True | 1 |
| tokh1242 | 0.00 | True | 1 |
| ukra1253 | 0.00 | True | 1 |
| umbr1253 | 0.00 | True | 1 |
| vlaa1240 | 0.00 | True | 1 |
| wakh1245 | 0.00 | True | 1 |
| wall1255 | 0.00 | True | 1 |
| wels1247 | 0.00 | True | 1 |
| west2354 | 0.00 | True | 1 |
| west2386 | 1.16 | False | 1 |
