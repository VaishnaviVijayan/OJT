import numpy as np
from django.http import JsonResponse
from django.shortcuts import render
import joblib
import os

# Load the model and preprocessor
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = joblib.load(os.path.join(BASE_DIR, 'predict/model/decision_tree_regressor.pkl'))
preprocesser = joblib.load(os.path.join(BASE_DIR, 'predict/model/preprocessor.pkl'))

def predict_yield(request):
    if request.method == 'POST':
        data = request.POST
        Year = int(data.get('Year'))
        average_rain_fall_mm_per_year = float(data.get('average_rain_fall_mm_per_year'))
        pesticides_tonnes = float(data.get('pesticides_tonnes'))
        avg_temp = float(data.get('avg_temp'))
        Area = data.get('Area')
        Item = data.get('Item')

        features = np.array([[Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item]], dtype=object)
        transform_features = preprocesser.transform(features)
        predicted_yield = model.predict(transform_features).reshape(-1, 1)
        result = predicted_yield[0][0]

        return JsonResponse({'predicted_yield': result})

    return render(request, 'form.html')
   