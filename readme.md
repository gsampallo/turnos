# Turnos
Get all watering shift from Irrigacion Mendoza Page and send notification to you

## Configuration file

```
{
    "database":"sqlite:///database.db",
    "logFolder":"log"
}
```

Need to set three environment variables:
```
export LASTNAME=lastname 
export CHANNEL=channel on ntfy
export sandbox= 1 or 0 if it's sandbox
```


## Dependencies
Run
```
pip install --no-cache-dir -r requirements.txt
```

## Run
First run for create the database tables.
```
python3 run_first.py
```

Schedule turnos2.py for run every hour.
