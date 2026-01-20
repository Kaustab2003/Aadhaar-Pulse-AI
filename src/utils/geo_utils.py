# Comprehensive dictionary for Indian Districts and States (Hackathon Demo Support)
# Includes State Centers for Fallback and Major Districts

DISTRICT_COORDS = {
    # --- UTs & Major Metros ---
    'Delhi': {'lat': 28.7041, 'lon': 77.1025},
    'New Delhi': {'lat': 28.6139, 'lon': 77.2090},
    'Central Delhi': {'lat': 28.6453, 'lon': 77.2456},
    'North Delhi': {'lat': 28.7243, 'lon': 77.2185},
    'South Delhi': {'lat': 28.4817, 'lon': 77.2625},
    'Chandigarh': {'lat': 30.7333, 'lon': 76.7794},

    # --- Andhra Pradesh ---
    'Andhra Pradesh': {'lat': 15.9129, 'lon': 79.7400},
    'Visakhapatnam': {'lat': 17.6868, 'lon': 83.2185},
    'Vijayawada': {'lat': 16.5062, 'lon': 80.6480},
    'Guntur': {'lat': 16.3067, 'lon': 80.4365},
    'Nellore': {'lat': 14.4426, 'lon': 79.9865},
    'Kurnool': {'lat': 15.8281, 'lon': 78.0373},
    'Chittoor': {'lat': 13.2172, 'lon': 79.1003},
    'Anantapur': {'lat': 14.6819, 'lon': 77.6006},
    'Tirupati': {'lat': 13.6288, 'lon': 79.4192},
    'East Godavari': {'lat': 16.9479, 'lon': 82.2395},

    # --- Arunachal Pradesh ---
    'Arunachal Pradesh': {'lat': 28.2180, 'lon': 94.7278},
    'Itanagar': {'lat': 27.0844, 'lon': 93.6053},
    'Tawang': {'lat': 27.5861, 'lon': 91.8594},
    'West Kameng': {'lat': 27.2764, 'lon': 92.4276},

    # --- Assam ---
    'Assam': {'lat': 26.2006, 'lon': 92.9376},
    'Guwahati': {'lat': 26.1445, 'lon': 91.7364},
    'Dispur': {'lat': 26.1430, 'lon': 91.7898},
    'Dibrugarh': {'lat': 27.4728, 'lon': 94.9120},
    'Jorhat': {'lat': 26.7509, 'lon': 94.2037},
    'Silchar': {'lat': 24.8333, 'lon': 92.7789},
    'Tezpur': {'lat': 26.6528, 'lon': 92.7926},
    'Nagaon': {'lat': 26.3480, 'lon': 92.6841},
    'Tinsukia': {'lat': 27.4886, 'lon': 95.3558},

    # --- Bihar ---
    'Bihar': {'lat': 25.0961, 'lon': 85.3131},
    'Patna': {'lat': 25.5941, 'lon': 85.1376},
    'Gaya': {'lat': 24.7914, 'lon': 85.0002},
    'Muzaffarpur': {'lat': 26.1209, 'lon': 85.3647},
    'Bhagalpur': {'lat': 25.2425, 'lon': 87.0111},
    'Darbhanga': {'lat': 26.1542, 'lon': 85.8918},
    'Purnia': {'lat': 25.7771, 'lon': 87.4753},
    'Begusarai': {'lat': 25.4182, 'lon': 86.1272},
    'Sitamarhi': {'lat': 26.5937, 'lon': 85.4850},
    'Madhubani': {'lat': 26.3483, 'lon': 86.0718},
    'Purbi Champaran': {'lat': 26.6473, 'lon': 84.9090},

    # --- Chhattisgarh ---
    'Chhattisgarh': {'lat': 21.2787, 'lon': 81.8661},
    'Raipur': {'lat': 21.2514, 'lon': 81.6296},
    'Bhilai': {'lat': 21.1938, 'lon': 81.3509},
    'Bilaspur': {'lat': 22.0797, 'lon': 82.1409},
    'Korba': {'lat': 22.3569, 'lon': 82.6807},
    'Durg': {'lat': 21.1904, 'lon': 81.2849},

    # --- Goa ---
    'Goa': {'lat': 15.2993, 'lon': 74.1240},
    'Panaji': {'lat': 15.4909, 'lon': 73.8278},
    'South Goa': {'lat': 15.2037, 'lon': 74.0503},
    'North Goa': {'lat': 15.5492, 'lon': 73.8797},

    # --- Gujarat ---
    'Gujarat': {'lat': 22.2587, 'lon': 71.1924},
    'Ahmedabad': {'lat': 23.0225, 'lon': 72.5714},
    'Surat': {'lat': 21.1702, 'lon': 72.8311},
    'Vadodara': {'lat': 22.3072, 'lon': 73.1812},
    'Rajkot': {'lat': 22.3039, 'lon': 70.8022},
    'Gandhinagar': {'lat': 23.2156, 'lon': 72.6369},
    'Bhavnagar': {'lat': 21.7645, 'lon': 72.1519},
    'Jamnagar': {'lat': 22.4707, 'lon': 70.0577},
    'Kutch': {'lat': 23.2420, 'lon': 69.6669},
    'Banas Kantha': {'lat': 24.1724, 'lon': 72.4387},

    # --- Haryana ---
    'Haryana': {'lat': 29.0588, 'lon': 76.0856},
    'Gurugram': {'lat': 28.4595, 'lon': 77.0266},
    'Faridabad': {'lat': 28.4089, 'lon': 77.3178},
    'Panipat': {'lat': 29.3909, 'lon': 76.9635},
    'Ambala': {'lat': 30.3782, 'lon': 76.7767},
    'Karnal': {'lat': 29.6857, 'lon': 76.9905},
    'Rohtak': {'lat': 28.8955, 'lon': 76.6066},
    'Hisar': {'lat': 29.1492, 'lon': 75.7217},

    # --- Himachal Pradesh ---
    'Himachal Pradesh': {'lat': 31.1048, 'lon': 77.1734},
    'Shimla': {'lat': 31.1048, 'lon': 77.1734},
    'Manali': {'lat': 32.2396, 'lon': 77.1887},
    'Dharamshala': {'lat': 32.2190, 'lon': 76.3234},
    'Kangra': {'lat': 32.0998, 'lon': 76.2691},

    # --- Jharkhand ---
    'Jharkhand': {'lat': 23.6102, 'lon': 85.2799},
    'Ranchi': {'lat': 23.3441, 'lon': 85.3096},
    'Jamshedpur': {'lat': 22.8046, 'lon': 86.2029},
    'Dhanbad': {'lat': 23.7957, 'lon': 86.4304},
    'Bokaro': {'lat': 23.6693, 'lon': 86.1511},
    'Hazaribagh': {'lat': 23.9936, 'lon': 85.3601},

    # --- Karnataka ---
    'Karnataka': {'lat': 15.3173, 'lon': 75.7139},
    'Bengaluru Urban': {'lat': 12.9716, 'lon': 77.5946},
    'Bengaluru': {'lat': 12.9716, 'lon': 77.5946},
    'Mysuru': {'lat': 12.2958, 'lon': 76.6394},
    'Mysore': {'lat': 12.2958, 'lon': 76.6394},
    'Hubli': {'lat': 15.3647, 'lon': 75.1240},
    'Mangaluru': {'lat': 12.9141, 'lon': 74.8560},
    'Belagavi': {'lat': 15.8497, 'lon': 74.4977},
    'Belgaum': {'lat': 15.8497, 'lon': 74.4977},
    'Kalaburagi': {'lat': 17.3297, 'lon': 76.8343},
    'Shivamogga': {'lat': 13.9299, 'lon': 75.5681},
    'Tumakuru': {'lat': 13.3392, 'lon': 77.1017},

    # --- Kerala ---
    'Kerala': {'lat': 10.8505, 'lon': 76.2711},
    'Thiruvananthapuram': {'lat': 8.5241, 'lon': 76.9366},
    'Kochi': {'lat': 9.9312, 'lon': 76.2673},
    'Kozhikode': {'lat': 11.2588, 'lon': 75.7804},
    'Thrissur': {'lat': 10.5276, 'lon': 76.2144},
    'Kannur': {'lat': 11.8745, 'lon': 75.3704},
    'Kollam': {'lat': 8.8932, 'lon': 76.6141},
    'Ernakulam': {'lat': 9.9816, 'lon': 76.2999},

    # --- Madhya Pradesh ---
    'Madhya Pradesh': {'lat': 22.9734, 'lon': 78.6569},
    'Bhopal': {'lat': 23.2599, 'lon': 77.4126},
    'Indore': {'lat': 22.7196, 'lon': 75.8577},
    'Gwalior': {'lat': 26.2183, 'lon': 78.1828},
    'Jabalpur': {'lat': 23.1815, 'lon': 79.9864},
    'Ujjain': {'lat': 23.1765, 'lon': 75.7885},
    'Sagar': {'lat': 23.8388, 'lon': 78.7378},
    'Rewa': {'lat': 24.5247, 'lon': 81.2998},
    
    # --- Maharashtra ---
    'Maharashtra': {'lat': 19.7515, 'lon': 75.7139},
    'Mumbai': {'lat': 19.0760, 'lon': 72.8777},
    'Pune': {'lat': 18.5204, 'lon': 73.8567},
    'Nagpur': {'lat': 21.1458, 'lon': 79.0882},
    'Nashik': {'lat': 19.9975, 'lon': 73.7898},
    'Thane': {'lat': 19.2183, 'lon': 72.9781},
    'Aurangabad': {'lat': 19.8762, 'lon': 75.3433},
    'Solapur': {'lat': 17.6599, 'lon': 75.9064},
    'Kolhapur': {'lat': 16.7050, 'lon': 74.2433},
    'Amravati': {'lat': 20.9320, 'lon': 77.7523},
    'Jalgaon': {'lat': 21.0077, 'lon': 75.5626},

    # --- Meghalaya ---
    'Meghalaya': {'lat': 25.4670, 'lon': 91.3662},
    'Shillong': {'lat': 25.5788, 'lon': 91.8933},
    'East Khasi Hills': {'lat': 25.4670, 'lon': 91.3662},
    'West Garo Hills': {'lat': 25.5141, 'lon': 90.2030},

    # --- Odisha ---
    'Odisha': {'lat': 20.9517, 'lon': 85.0985},
    'Bhubaneswar': {'lat': 20.2961, 'lon': 85.8245},
    'Cuttack': {'lat': 20.4625, 'lon': 85.8828},
    'Rourkela': {'lat': 22.2604, 'lon': 84.8536},
    'Berhampur': {'lat': 19.3150, 'lon': 84.7941},
    'Sambalpur': {'lat': 21.4669, 'lon': 83.9812},
    'Puri': {'lat': 19.8135, 'lon': 85.8312},
    'Ganjam': {'lat': 19.3541, 'lon': 84.9783},

    # --- Punjab ---
    'Punjab': {'lat': 31.1471, 'lon': 75.3412},
    'Ludhiana': {'lat': 30.9010, 'lon': 75.8573},
    'Amritsar': {'lat': 31.6340, 'lon': 74.8723},
    'Jalandhar': {'lat': 31.3260, 'lon': 75.5762},
    'Patiala': {'lat': 30.3398, 'lon': 76.3869},
    'Bathinda': {'lat': 30.2110, 'lon': 74.9455},

    # --- Rajasthan ---
    'Rajasthan': {'lat': 27.0238, 'lon': 74.2179},
    'Jaipur': {'lat': 26.9124, 'lon': 75.7873},
    'Jodhpur': {'lat': 26.2389, 'lon': 73.0243},
    'Udaipur': {'lat': 24.5854, 'lon': 73.7125},
    'Kota': {'lat': 25.2138, 'lon': 75.8648},
    'Ajmer': {'lat': 26.4499, 'lon': 74.6399},
    'Bikaner': {'lat': 28.0229, 'lon': 73.3119},
    'Alwar': {'lat': 27.5530, 'lon': 76.6346},
    'Sikar': {'lat': 27.6094, 'lon': 75.1398},
    'Bhilwara': {'lat': 25.3216, 'lon': 74.5868},
    
    # --- Sikkim ---
    'Sikkim': {'lat': 27.5330, 'lon': 88.5122},
    'Gangtok': {'lat': 27.3389, 'lon': 88.6065},

    # --- Tamil Nadu ---
    'Tamil Nadu': {'lat': 11.1271, 'lon': 78.6569},
    'Chennai': {'lat': 13.0827, 'lon': 80.2707},
    'Coimbatore': {'lat': 11.0168, 'lon': 76.9558},
    'Madurai': {'lat': 9.9252, 'lon': 78.1198},
    'Tiruchirappalli': {'lat': 10.7905, 'lon': 78.7047},
    'Salem': {'lat': 11.6643, 'lon': 78.1460},
    'Tiruppur': {'lat': 11.1085, 'lon': 77.3411},
    'Erode': {'lat': 11.3410, 'lon': 77.7172},
    'Vellore': {'lat': 12.9165, 'lon': 79.1325},
    'Kancheepuram': {'lat': 12.8185, 'lon': 79.7107},
    'Kanyakumari': {'lat': 8.0883, 'lon': 77.5385},

    # --- Telangana ---
    'Telangana': {'lat': 18.1124, 'lon': 79.0193},
    'Hyderabad': {'lat': 17.3850, 'lon': 78.4867},
    'Warangal': {'lat': 17.9689, 'lon': 79.5941},
    'Nizamabad': {'lat': 18.6725, 'lon': 78.0941},
    'Karimnagar': {'lat': 18.4386, 'lon': 79.1288},
    'Khammam': {'lat': 17.2473, 'lon': 80.1514},

    # --- Uttar Pradesh ---
    'Uttar Pradesh': {'lat': 26.8467, 'lon': 80.9462},
    'Lucknow': {'lat': 26.8467, 'lon': 80.9462},
    'Kanpur': {'lat': 26.4499, 'lon': 80.3319},
    'Kanpur Nagar': {'lat': 26.4499, 'lon': 80.3319},
    'Ghaziabad': {'lat': 28.6692, 'lon': 77.4538},
    'Agra': {'lat': 27.1767, 'lon': 78.0081},
    'Varanasi': {'lat': 25.3176, 'lon': 82.9739},
    'Meerut': {'lat': 28.9845, 'lon': 77.7064},
    'Prayagraj': {'lat': 25.4358, 'lon': 81.8463},
    'Allahabad': {'lat': 25.4358, 'lon': 81.8463},
    'Bareilly': {'lat': 28.3670, 'lon': 79.4304},
    'Aligarh': {'lat': 27.8974, 'lon': 78.0880},
    'Moradabad': {'lat': 28.8386, 'lon': 78.7733},
    'Saharanpur': {'lat': 29.9640, 'lon': 77.5460},
    'Gorakhpur': {'lat': 26.7606, 'lon': 83.3732},
    'Gautam Buddha Nagar': {'lat': 28.5355, 'lon': 77.3910},
    'Noida': {'lat': 28.5355, 'lon': 77.3910},
    'Ayodhya': {'lat': 26.7924, 'lon': 82.1998},
    'Mathura': {'lat': 27.4924, 'lon': 77.6737},
    'Jhansi': {'lat': 25.4484, 'lon': 78.5685},

    # --- Uttarakhand ---
    'Uttarakhand': {'lat': 30.0668, 'lon': 79.0193},
    'Dehradun': {'lat': 30.3165, 'lon': 78.0322},
    'Haridwar': {'lat': 29.9457, 'lon': 78.1642},
    'Nainital': {'lat': 29.3919, 'lon': 79.4542},
    'Rishikesh': {'lat': 30.0869, 'lon': 78.2676},

    # --- West Bengal ---
    'West Bengal': {'lat': 22.9868, 'lon': 87.8550},
    'Kolkata': {'lat': 22.5726, 'lon': 88.3639},
    'Howrah': {'lat': 22.5958, 'lon': 88.2636},
    'Siliguri': {'lat': 26.7271, 'lon': 88.3953},
    'Durgapur': {'lat': 23.5204, 'lon': 87.3119},
    'Asansol': {'lat': 23.6739, 'lon': 86.9524},
    'Darjeeling': {'lat': 27.0410, 'lon': 88.2663},
    'Coochbehar': {'lat': 26.3262, 'lon': 89.4475},
    'Malda': {'lat': 25.0440, 'lon': 88.1360},
    'Hooghly': {'lat': 22.8950, 'lon': 88.4060},
    'Paschim Medinipur': {'lat': 22.4284, 'lon': 87.3197}
}

def get_lat_lon(district_name, state_name=None):
    """
    Returns (lat, lon) for a district. 
    Fallbacks:
    1. Exact District Match
    2. Approximate State Center + Jitter (to prevent overlap)
    """
    # 1. Direct Match
    if district_name in DISTRICT_COORDS:
        return DISTRICT_COORDS[district_name]
    
    # 2. State Fallback
    if state_name and state_name in DISTRICT_COORDS:
        import random
        # Base coordinates of State
        base = DISTRICT_COORDS[state_name]
        
        # Add seeded random jitter so points in same state don't stack perfectly
        # Use district name hash for consistent jitter for same district
        random.seed(district_name) 
        
        # Jitter range: +/- 0.5 degrees (approx 50km)
        # Allows points to scatter around the state center
        lat_jitter = random.uniform(-0.5, 0.5)
        lon_jitter = random.uniform(-0.5, 0.5)
        
        return {
            'lat': base['lat'] + lat_jitter,
            'lon': base['lon'] + lon_jitter
        }
        
    # Return nothing if both fail (filtered out in UI)
    return None
