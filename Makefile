.PHONY: release tag
.SILENT: release tag

# Command-line argument for version (v) - Only used for 'release' command
v ?= $(shell grep -Po '(?<=^__version__ = ")([0-9]+\.[0-9]+\.[0-9]+)' aichatcoder/__init__.py)

# Ensure the version is prefixed with "v" for tagging
TAG = $(shell echo $(v) | sed 's/^v*//')  # Removes any existing 'v'
TAG = v$(TAG)  # Adds 'v' prefix

increment_patch = $(shell echo $(v) | awk -F. '{print $$1"."$$2"."$$$$(NF)+1}')

release:
	@if [ "$(v)" = "" ]; then \
		echo "No version specified. Attempting to read from __init__.py..."; \
		v=$(shell grep -Po '(?<=^__version__ = ")([0-9]+\.[0-9]+\.[0-9]+)' aichatcoder/__init__.py); \
		echo "Last version found: $$v"; \
		v=$(increment_patch); \
		echo "Auto-incremented patch version: $$v"; \
		read -p "Do you want to proceed with version $$v? (y/n): " confirm && if [ "$$confirm" != "y" ]; then exit 1; fi; \
	fi;

	@echo "Releasing version $(v)..."

	# 1. Update version in aichatcoder/__init__.py
	@sed -i "s/^__version__ = .*/__version__ = \"$(v)\"/" aichatcoder/__init__.py

	# 2. Update version in pyproject.toml
	@sed -i "s/^version = .*/version = \"$(v)\"/" pyproject.toml

	# 3. Commit the changes
	@git add .
	@git commit -m "updated for release $(v)"
	@git push

	@echo "Version $(v) released successfully."

tag:
	v=$(shell grep -Po '(?<=^__version__ = ")([0-9]+\.[0-9]+\.[0-9]+)' aichatcoder/__init__.py)
	@read -p "Do you want to create a tag for version ${v}? (y/n): " TAG_CONFIRM && if [ "$$TAG_CONFIRM" != "y" ]; then exit 1; fi;

	@echo "Tagging version $$TAG..."

	# Create the tag
	@git tag $$TAG

	# Push the tag to origin
	@git push origin $$TAG

	@echo "Version $$TAG tagged and pushed successfully."
