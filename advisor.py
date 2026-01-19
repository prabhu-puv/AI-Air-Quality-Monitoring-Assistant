def air_quality_advisor(aqi):
    if aqi <= 50:
        level = "Good"
        advice = "Air quality is good. Safe for outdoor activities."
    elif aqi <= 100:
        level = "Moderate"
        advice = "Air quality is acceptable. Sensitive people should be cautious."
    elif aqi <= 200:
        level = "Poor"
        advice = "Avoid prolonged outdoor activities. People with breathing problems should stay indoors."
    elif aqi <= 300:
        level = "Very Poor"
        advice = "Wear a mask and avoid going outside if possible."
    else:
        level = "Severe"
        advice = "Health emergency. Stay indoors and keep windows closed."

    return level, advice
