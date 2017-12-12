## ModelDB Demo
---
@title[1. Launch docker-compose]

### <span class="step-title">#1. Docker compose</span>
<br>

```shell

$ git clone https://github.com/engapa/modeldb-demo.git
$ cd modeldb-demo

$ docker-compose version
$ docker-compose up

Done!
```

@[2-3](Clone this repo)
@[5](Check docker-compose is installed on your local machine or VM)
@[6](Launch docker-compose command to run modeldb components)
@[8](Everything goes well ...)
---
@title[2. Check frontend]

### <span class="step-title">#2. Check frontend is running</span>
<br>

[http://localhost:3000 @fa[external-link]](http://localhost:3000)
---
@title[3. Install python basic client ]

### <span class="step-title">#3. Install python basic client</span>
<br>

```shell
$ docker run -it -d -v $(pwd)/python:/modeldb-python \
  --network host python:3.6 bash
$ pip install modeldb-basic
$ pip list --format legacy | grep modeldb
```

@[1-2](Run a python 3.6 container)
@[3](Install modeldb basic client)
@[4](Ensure modeldb basic client was installed successfully)
---?code=python/BasicSync.py&lang=python&title=#4. Send model data

@[1-3](Import client classes)
@[5](Create a main object to transfer model information - see syncer.json file)
@[7-11](Partial sync of data sets)
@[13,15-17,19-21](Partial sync of a couple of models with different configurations)
@[23-26](Partial sync of metrics for both models)
@[28](Effective transmission of all model data)
@[29](Execute "python BasicSync.py")

---?code=python/BasicSyncAll.py&lang=python&title=#5. Send model data from file
@[1](Import client dependencies)
@[4-7](Create a new project, if it doesn't exist yet)
@[10](Sync all information from file - see YamlExperimentMetrics.yaml)
@[12](Effective transmission of all model data)
@[13](Execute "python BasicSyncAll.py")

---
@title[6. Using scikit-learn client]

- Install modeldb package instead of modeldb-basic
- Event objects enable us to track data sets and metric changes
- "_sync" methods overrides native scikit-learn methods
- Samples are available at [upstream project @fa[external-link]](https://github.com/mitdbg/modeldb/tree/master/client/python/samples/sklearn)

---
## Thanks everyone !!