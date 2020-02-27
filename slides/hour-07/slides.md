# HOUR 7

Setting up a machine learning project with cookiecutter templates

---

## Why you need a better setup for your project

---~

## The challenge of using notebooks in your projects

* Order of execution is not guaranteed
* Merging is impossible
* Can't be run from a build pipeline

---~

### Quality goals for a typical ML project

* Maintainable code
* Reproducable results
* Tracable results

---~

### 5 steps for a better ML project:

1. Treat your data as immutable
2. Save intermediate steps
3. Track logging information
4. Build your project as a package
5. Use a build tool

---~

### Treat your dataset as immutable

* Overwriting data is a big no-no.
* What happens if you make a mistake?

---~

### Save intermediate results

* Sometimes you need to re-run
* Easier if you have intermediate results

---~

### Log information

* Programs wil break!
* Logging will save you a lot of time debugging

---~

### Logging using structlog

```
pip install structlog
```

```
import structlog

log = structlog.get_logger()
log.info('Informational message', key=value)
log.warn('...')
log.error('Woops!')
```

<small>http://www.structlog.org/en/stable/</small>

---~

### Turn your project into a proper package

Moves away from "works on my machine"
towards a more friendly, works everywhere.

---~

### Define a build pipeline for your project

Allows you to define the order for the scripts.

Use whatever you like, for example:
* Makefile  <!-- .element: class="fragment" -->
* Psake <!-- .element: class="fragment" -->

Note: 
Makefile tutorial https://krzysztofzuraw.com/blog/2016/makefiles-in-python-projects.html
Psake website https://github.com/psake/psake
---

## Setting up your data science project with the data science cookiecutter 

---~

### A quick introduction to cookiecutter

A templating tool for creating python projects

```
pip install cookiecutter
```

```
cookiecutter <template-url>
```

---~

### The data science template

https://drivendata.github.io/cookiecutter-data-science/
