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

@[1](Clone this repo)
@[3](Check docker-compose is installed on your local machine or VM)
@[4](Launch docker-compose command to run modeldb components)
@[6](Everything goes well ...)
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

@[1](Run a python 3.6 container)
@[3](Install modeldb basic client)
@[4](Ensure modeldb basic client was installed successfully)
---?code=python/BasicSync.py&lang=python&title=4. Send model data

@[1](Proba proba)

---?code=python/BasicSyncAll.py&lang=python&title=5. Send model data from file
