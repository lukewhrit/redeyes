PYTHON ?= python3
PYSOURCES := redeyes

.PHONY: develop
develop:
	DEBUG=true $(PYTHON) -m flask --app $(PYSOURCES)/wsgi.py run

.PHONY: venv
venv:
	$(PYTHON) -m venv .venv
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

.PHONY: production
production:
	$(PYTHON) -m gunicorn $(PYSOURCES).wsgi

.PHONY: test
test:
	$(PYTHON) -m coverage run -m pytest $(PYTESTFLAGS)

.PHONY: lint
lint:
	$(PYTHON) -m flake8 --show-source $(PYSOURCES)/
	$(PYTHON) -m isort --check $(PYSOURCES)/

.PHONY: fix
fix:
	$(PYTHON) -m isort --quiet $(PYSOURCES)/
