# Deploying to Google Cloud Platform (GCP)

Since this is a static site (HTML/CSS/JS), the most cost-effective and scalable way to host it on GCP is using a **Cloud Storage Bucket**.

## Prerequisites

1.  [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed and authenticated (`gcloud auth login`).
2.  A valid billing account and project.

## Step-by-Step Guide

### 1. Create a Bucket

Replace `your-bucket-name` with a unique name (e.g., `my-portfolio-2025`).

```bash
# Create the bucket (US region for example)
gcloud storage buckets create gs://your-bucket-name --location=US
```

### 2. Make the Bucket Public

**Note:** This makes all files in the bucket accessible to the internet.

```bash
# Allow public read access
gcloud storage buckets add-iam-policy-binding gs://your-bucket-name \
    --member=allUsers \
    --role=roles/storage.objectViewer
```

### 3. Upload Your Files

Navigate to your project folder:
`c:/Users/migue/Documents/github/portfolio`

Upload all files recursively:

```bash
gcloud storage cp -r . gs://your-bucket-name
```

### 4. Set the Website Configuration

Tell GCP which file is the main page (`index.html`) and error page.

```bash
gcloud storage buckets update gs://your-bucket-name --web-main-page-suffix=index.html --web-error-page=index.html
```

### 5. Access Your Site

Your website will be available at:

`https://storage.googleapis.com/your-bucket-name/index.html`

### (Optional) Custom Domain

To use a custom domain (e.g., `www.yourname.com`):
1.  Verify domain ownership in Google Search Console.
2.  Name your bucket exactly like your domain (e.g., `www.yourname.com`).
3.  Create a CNAME record in your DNS provider pointing `www` to `c.storage.googleapis.com`.
