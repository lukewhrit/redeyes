PYTHON ?= python3
PYSOURCES := redeyes/

.PHONY: develop
develop:
	$(PYTHON) -m pip install --editable .[all]


.PHONY: develop
production:
	$(PYTHON) -m pip install --editable .[all]

.PHONY: test
test:
	$(PYTHON) -m coverage run -m pytest $(PYTESTFLAGS)

.PHONY: lint
lint:
	$(PYTHON) -m flake8 --show-source $(PYSOURCES)
	$(PYTHON) -m isort --check $(PYSOURCES)

.PHONY: fix
fix:
	$(PYTHON) -m isort --quiet $(PYSOURCES)
