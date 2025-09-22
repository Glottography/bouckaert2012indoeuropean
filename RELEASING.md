# Releasing the dataset

## Recreate the raw data from glottography-data

```shell
cldfbench download cldfbench_bouckaert2012indoeuropean.py
```

## Recreate the CLDF data

```shell
cldfbench makecldf cldfbench_bouckaert2012indoeuropean.py --glottolog-version v5.2
cldfbench cldfreadme cldfbench_bouckaert2012indoeuropean.py
cldfbench zenodo --communities glottography cldfbench_bouckaert2012indoeuropean.py
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
cldfbench geojson.glottolog_distance cldf --format tsv | csvformat -t | csvgrep -c Distance -r"^0\.?" -i | csvsort -c Distance | csvcut -c ID,Distance | csvformat -E | termgraph
```

```
west2386: ▇▇ 1.17 
scot1243: ▇▇▇ 1.44 
chur1257: ▇▇▇ 1.48 
anci1242: ▇▇▇▇ 2.17 
mode1248: ▇▇▇▇▇ 2.82 
oriy1255: ▇▇▇▇▇▇ 3.00 
prus1238: ▇▇▇▇▇▇▇ 3.47 
sans1269: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 7.61 
goth1244: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 13.12
oldn1244: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 23.94
```