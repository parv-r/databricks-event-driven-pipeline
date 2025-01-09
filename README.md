## Databricks Workflow for File Ingestion, Staging, and Merging from GCP Storage

This repository demonstrates a complete workflow to automate file ingestion from a Google Cloud Storage (GCS) bucket into Databricks. The workflow processes the uploaded files by loading the data into a staging table, backing up the files into an archive folder, and performing an upsert (merge) operation into a target table.

### Workflow Overview

The automated process includes the following steps:
  - Monitor a Google Cloud Storage (GCS) bucket for new file uploads.
  - Load the data into a staging table in Databricks.
  - Archive the processed file into a dedicated folder in the GCS bucket.
  - Merge the data from the staging table into the target table in Databricks.

### Steps to Set Up

#### 1. Google Cloud Storage Setup
- Create a GCS bucket with two folders:
- source: Holds the incoming files.
- archive: Stores archived files after processing.

#### 2. External Data Source in Databricks
  - Create an external data source in Databricks and link it to the GCS bucket created in Step 1.

#### 3. Databricks Catalog and Volume
  - Create a new catalog in Databricks for organizing data assets.
  - Within the catalog:
  - Create a volume linked to the external data source to replicate the GCS bucket hierarchy.

#### 4. Git Integration
  1. Create a Git repository (e.g., on GitHub) for version control.
  2. Link the Databricks workspace to the Git repository:
	  - Initialize a dev branch to make changes.
	  - Merge changes into the main branch after testing and validation.

#### 5. Notebooks for Data Processing
  - Create two notebooks in the dev branch:
    1. Stage Table Load and Archival Notebook:
      - Handles file ingestion from the GCS bucket.
      - Loads data into the stage table.
      - Archives processed files into the archive folder.
    2. Merge Data Notebook:
      - Merges the data from the stage table into the target table using an upsert operation.

#### 6. Workflow Creation
  - Create a Databricks Workflow:
  - Add the notebooks as individual tasks in the workflow.
  - Set dependencies as needed between tasks.

#### 7. Testing and Deployment
  1. Run the workflow manually once to validate its functionality.
  2. Ensure the workflow is triggered automatically whenever a new file is uploaded to the source folder in the GCS bucket.


#### Key Features
  - Real-Time File Ingestion: Automatically processes files uploaded to the GCS bucket.
  - Data Backup: Ensures all processed files are archived for traceability and recovery.
  - Upsert Logic: Efficiently merges data into the target table to maintain a single source of truth.
  - Scalable Architecture: Built with cloud storage and Databricks to handle large volumes of data.

#### Technologies Used
  - Google Cloud Storage (GCS)
  - Databricks (Catalog, Volumes, Workflows)
  - Python (Databricks Notebooks)
  - Git (Version Control)

#### How to Contribute
  1. Clone the repository.
  2. Create a new feature branch from the dev branch.
  3. Commit your changes and create a pull request for review.
  4. Ensure all workflows are tested before merging into main.