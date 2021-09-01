import time
import requests


LOC_NAMES = {
    "cd26be38-1a73-eb11-b1ac-00224814f9a4": ["Albury Wodonga Health VIC", "3690"],
    "e0a02973-e7c8-eb11-bacc-00224817f5e2": [
        "Alfred Health - Pfizer Community Clinic VIC",
        "3004",
    ],
    "b726be38-1a73-eb11-b1ac-00224814f9a4": ["Austin - Olivia Newton John VIC", "3084"],
    "3acc7322-12f0-eb11-94ef-00224814e3f2": [
        "Austin - Repatriation (Pfizer) VIC",
        "3084",
    ],
    "75dc1ee4-90c2-eb11-bacc-002248183178": ["Bairnsdale City Oval VIC", "3875"],
    "bc3eafdd-0b8d-eb11-b1ac-002248155d0e": ["Ballan Vaccination Clinic VIC", "3342"],
    "39779e5d-1a73-eb11-b1ac-000d3a791111": [
        "Ballarat Community Clinic- Pfizer VIC",
        "3350",
    ],
    "e28a5298-06db-eb11-bacb-0022481581e9": ["Beechworth Vaccination Hub VIC", "3747"],
    "8526be38-1a73-eb11-b1ac-00224814f9a4": ["Bendigo Health VIC", "3550"],
    "ce190a0f-9dbe-eb11-bacc-002248151230": ["Box Hill Hospital Pfizer VIC", "3128"],
    "15540e42-c5da-eb11-bacb-0022481581e9": ["Bright Hub - North East VIC", "3741"],
    "54782623-5de4-eb11-bacb-002248185c40": ["Casterton Memorial Hospital VIC", "3311"],
    "754d9be1-997c-eb11-a812-00224814d29f": ["Castlemaine Health VIC", "3450"],
    "c5cf4b1b-c786-eb11-a812-0022481532ac": [
        "Convention Centre South Wharf VIC",
        "3006",
    ],
    "ff77c470-507d-eb11-a812-00224814de29": ["Corryong health VIC", "3707"],
    "33bda98d-eda6-eb11-9442-002248153030": ["Cranbourne Turf Club VIC", "3977"],
    "1f779e5d-1a73-eb11-b1ac-000d3a791111": ["Dandenong Hospital VIC", "3175"],
    "bdd19c7c-94ef-eb11-94ef-00224814ef7c": ["Darlingsford Barn - Melton VIC", "3337"],
    "60f950b1-d486-eb11-a812-0022481536df": [
        "East Grampians Health Services- Ararat VIC",
        "3377",
    ],
    "93aecf72-5ae4-eb11-bacb-002248185c40": [
        "Ford, Barwon Health Geelong, VIC",
        "3214",
    ],
    "0c9895d7-4bd9-eb11-bacb-002248158a34": [
        "Frankston Community Vaccination Hub - Bayside Centre VIC",
        "3199",
    ],
    "b106508f-9bb6-eb11-8236-00224814f89c": [
        "Gippsland Regional Sports Complex - Sale VIC",
        "3850",
    ],
    "b904b83c-4fbf-eb11-bacc-002248151d2b": [
        "Goods Shed Warragul Railway Station VIC",
        "3820",
    ],
    "272f8516-0c8d-eb11-b1ac-00224815503b": ["Horsham VIC", "3400"],
    "9fd3f9d6-82ea-eb11-bacb-00224814b728": ["Hotel Quarantine – AHC VIC", "3004"],
    "95231fcf-6d8b-eb11-b1ac-00224815571e": [
        "Kilmore District Health Sub Hub VIC",
        "3764",
    ],
    "a71c7cbf-7fcd-eb11-bacc-002248152898": ["Knox Private Hospital VIC", "3152"],
    "6b798794-b587-eb11-a812-002248153c69": [
        "Kyabram District Health Service VIC",
        "3620",
    ],
    "36ac30b2-9ed7-eb11-bacb-002248158a34": ["Leongatha Community Clinic VIC", "3953"],
    "23779e5d-1a73-eb11-b1ac-000d3a791111": [
        "Macintosh Center-Shepparton Show grounds VIC",
        "3630",
    ],
    "5a5f4e66-638b-eb11-b1ac-0022481556c9": [
        "Mansfield District Hospital - Anderson Hall VIC",
        "3722",
    ],
    "819d2365-e9b1-eb11-8236-00224814b955": ["Melbourne Showgrounds VIC", "3032"],
    "8f8a4549-8ec9-eb11-bacc-00224817f355": ["Monash Community Outreach VIC", "3177"],
    "1d779e5d-1a73-eb11-b1ac-000d3a791111": ["Monash Medical Centre VIC", "3168"],
    "3a432e3e-c6da-eb11-bacb-0022481581e9": ["Mt Beauty Vaccination Hub VIC", "3699"],
    "d66d25ae-1dda-eb11-bacb-002248158ab0": ["Myrtleford Vaccination Hub VIC", "3737"],
    "e278faee-5985-eb11-a812-0022481532a0": ["NCN Health VIC", "3644"],
    "01527c87-7de0-eb11-bacb-0022481590f3": [
        "NH - Plenty Ranges Arts & Convention Centre VIC",
        "3752",
    ],
    "0f033489-bd92-eb11-b1ac-002248146050": ["Northeast Health Wangaratta VIC", "3677"],
    "16fe7d59-66ac-eb11-8236-00224814f95b": ["Orbost Regional Health VIC", "3888"],
    "e2f6fed3-fa8a-eb11-b1ac-002248155631": [
        "Peninsula Health – Theatre 10 VIC",
        "3199",
    ],
    "75c5fd15-0cb2-eb11-8236-00224814b44d": ["RMH Pfizer VIC", "3052"],
    "aa22a817-94ef-eb11-94ef-00224814ef7c": ["Rockbank Hall - Melton VIC", "3335"],
    "6e3cfeed-70b7-eb11-8236-00224814f171": [
        "Royal Exhibition Building - Pfizer VIC",
        "3053",
    ],
    "b10a95c0-eda6-eb11-9442-002248153030": ["Sandown Racecourse VIC", "3145"],
    "c3a8c233-a0c5-eb11-bacc-00224818354b": [
        "Sandringham Vaccination Centre, Sandringham VIC",
        "3191",
    ],
    "2b439785-6bad-eb11-8236-00224814ffd4": ["Seymour Health VIC", "3660"],
    "0b0b7a0f-c282-eb11-a812-0022481522dc": ["St John of God Berwick VIC", "3806"],
    "9df109eb-87e3-eb11-bacb-002248185ba6": [
        "Star Health - Betty Day Centre St Kilda VIC",
        "3182",
    ],
    "97e5a06d-f9cf-eb11-bacc-002248152898": [
        "Star Health - Horace Petty Centre South Yarra VIC",
        "3141",
    ],
    "13779e5d-1a73-eb11-b1ac-000d3a791111": ["Sunshine Hospital VIC", "3021"],
    "f7898e25-5fe4-eb11-bacb-002248185c40": ["SWH - Camperdown VIC", "3260"],
    "93772a43-1298-eb11-b1ac-002248153235": ["Traralgon Racecourse VIC", "3844"],
    "540abd49-5fe4-eb11-bacb-002248185c40": [
        "Warrnambool – SWH Vaccination Centre VIC",
        "3280",
    ],
    "f657e2fa-99b6-eb11-8236-00224814f89c": ["Wonthaggi Town Hall VIC", "3995"],
    "5d39fc61-12df-eb11-bacb-00224815988c": ["Wyndham Civic Centre VIC", "3030"],
    "d894247c-75bf-eb11-bacc-002248151546": ["Yarram Medical Centre VIC", "3971"],
}


COVID_QUEUE_API_ENDPOINT = (
    "https://apisuperboi.com/task/get_vic_covid_times/?h=AustraliaMelbourne271745945"
)
BREAKLINE = "\n\t"

while True:
    print("\033[2J")
    response = requests.get(COVID_QUEUE_API_ENDPOINT)

    if response.ok:
        results = response.json()

    for loc, data in results.items():
        if len(data["data"]):
            if loc not in LOC_NAMES:
                print(f"unknown loc: {loc}")
                raise KeyError(f"{loc} not a known clinic location")
            else:
                print(f"{LOC_NAMES[loc][1]} -> {LOC_NAMES[loc][0]}:\n\t{BREAKLINE.join(data['data'])}")

    time.sleep(5)
