## 🛠️ Setup Instructions

Follow the steps below to set up the project environment using Conda:

### 📦 Step 1: Create the Conda Environment

Open your terminal and run the following command to create the environment from the `environment.yml` file:

```bash
conda env create -f environment.yml

```

### Step 2: Activate the Environment

Once the environment is created, activate it with:

``` bash
conda activate resume_classifier_env
```

#### Add packages to environment.yml and recreate env
If you want your environment reproducible for the whole team:
Add the new packages to the dependencies section in your environment.yml.
Then run:
```bash
conda env update -f environment.yml --prune
```
#### Do you need to activate the environment again?
No — not necessarily, if the environment was already active when you ran the command.

However:
If you weren’t in the environment, or you're opening a new terminal/session, then yes, you’ll need to activate it again:
```bash
conda activate resume_classifier_env
```
