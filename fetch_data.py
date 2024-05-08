import asyncio
import aiohttp
import json
import os
from tqdm import tqdm

async def fetch_data(session, api_url):
    async with session.get(api_url) as response:
        try:
            response.raise_for_status()  # Raise exception for 4xx or 5xx status codes
            return await response.json()
        except Exception as e:
            print(f"Failed to fetch data from {api_url}: {e}")
            return None

async def fetch_batch_data(batch, progress_desc="Fetching data"):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, f"https://api.mfapi.in/mf/{scheme_code}") for scheme_code in batch]
        data = {}
        with tqdm(total=len(batch), desc=progress_desc, unit="scheme") as pbar:
            for future in asyncio.as_completed(tasks):
                scheme_data = await future
                if scheme_data is not None:
                    scheme_code = scheme_data.get('meta', {}).get('scheme_code')
                    data[scheme_code] = scheme_data
                pbar.update(1)
        return data

async def fetch_data_in_batches(start_scheme_code, end_scheme_code, batch_size=1000, progress_threshold=0.3):
    total_schemes = end_scheme_code - start_scheme_code + 1
    num_batches = total_schemes // batch_size + (1 if total_schemes % batch_size != 0 else 0)
    num_schemes_to_store = int(total_schemes * progress_threshold)
    schemes_fetched = 0
    data = {}

    for batch_index in tqdm(range(num_batches), desc="Overall Progress", unit="batch"):
        start = start_scheme_code + batch_index * batch_size
        end = min(start_scheme_code + (batch_index + 1) * batch_size - 1, end_scheme_code)
        batch = range(start, end + 1)
        
        # Fetch data for the current batch
        batch_data = await fetch_batch_data(batch, progress_desc=f"Batch {batch_index + 1}")
        
        # Store fetched data
        data.update(batch_data)
        schemes_fetched += len(batch_data)
        
        # Check if it's time to write to the folder
        if schemes_fetched >= num_schemes_to_store:
            # Write data to files
            await store_data_in_files(data, 'scheme_data')
            data = {}  # Clear data after storing
            
            # Update progress threshold for the next batch
            progress_threshold += 0.3
            num_schemes_to_store = int(total_schemes * progress_threshold)

async def store_data_in_files(data, folder_path):
    os.makedirs(folder_path, exist_ok=True)
    with tqdm(total=len(data), desc="Storing data", unit="scheme") as pbar:
        for scheme_code, scheme_data in data.items():
            if scheme_data:
                filename = os.path.join(folder_path, f"{scheme_code}.json")
                with open(filename, 'w') as file:
                    json.dump(scheme_data, file)
            else:
                print(f"Failed to fetch data for scheme code {scheme_code}")
            pbar.update(1)

# Define start and end scheme codes
start_scheme_code = 100027
end_scheme_code = 152607

# Fetch data for schemes in batches and periodically store

async def main():
    await fetch_data_in_batches(start_scheme_code, end_scheme_code)

# Run the asynchronous main function
asyncio.run(main())
