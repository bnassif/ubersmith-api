# Makefile for ubersmith-api
# Usage:
#		make generate_version SCHEMA_FILE=5.0.3.json	# build a version-speicifc client from a schema file
#		make generate_all															# build all version-specific clients from available schemas
#   make build				                  					# local dev build -> ./dist/ubersmith_api-$(VERSION){-py3-none-any.whl,powerdns-0.0.1.tar.gz}
#   make release VERSION=1.2-3					  				# full PyPi build flow to generate artifacts
#   make clean																		# clean artifacts from the ./dist directory

SHELL := bash
.ONESHELL:

# ---- Project metadata ----
PKG := ubersmith
VERSION ?= $(shell (git describe --tags --abbrev=0 2>/dev/null) || echo dev)

# ---- Paths ----
ROOT_DIR := .
OUT_ROOT := $(ROOT_DIR)/dist
SRC_DIR := $(ROOT_DIR)/src
PKG_DIR := $(SRC_DIR)/$(PKG)
VERSION_FILE := "$(ROOT_DIR)/src/$(PKG)/__version__.py"
SCHEMA_DIR := $(ROOT_DIR)/schema
SCHEMA_FILE ?= ""
SCHEMA_SCRIPT := "$(ROOT_DIR)/tools/generate_classes.py"

# ---- Helpers ----
define need
	@command -v $(1) >/dev/null 2>&1 || { echo "ERROR: missing dependency: $(1)"; exit 1; }
endef

# ---- Default target ----
.DEFAULT_GOAL := help

.PHONY: help
help: ## Show help
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make <target> [VERSION=X]\n\nTargets:\n"} \
	/^[a-zA-Z0-9_.-]+:.*##/ { printf "  %-18s %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.PHONY: version
version: ## Update the version in __version__.py
	sed -i 's|__version__ *= *"[^"]*"|__version__ = "$(VERSION)"|' $(VERSION_FILE)

# -------- Build Pipeline --------

.PHONY: generate_version
generate_version: # Generate a version specific module from a schema
	$(call need,python3)
	chmod +x "$(SCHEMA_SCRIPT)"
	"$(SCHEMA_SCRIPT)" -f "$(SCHEMA_FILE)"

.PHONY: generate_all
generate_all: # Generate version specific modules for all schemas
	$(call need,python3)
	chmod +x "$(SCHEMA_SCRIPT)"
	"$(SCHEMA_SCRIPT)"

# -------- Release pipeline --------
.PHONY: release
release: clean build

.PHONY: clean
clean: ## Remove existing distribution dir
	rm -rf "$(OUT_ROOT)"

.PHONY: build
build: version ## Build PyPi Package
	$(call need,python3)
	python3 -m build
