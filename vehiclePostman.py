import http.client
import json

conn = http.client.HTTPSConnection("tspvahan.tspolice.gov.in")
payload = ''
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5ODk0ZGQ5OC1jZmQwLTQzYzktOTBmZi05NDcyNjAyYzBkMmUiLCJqdGkiOiJiMDI2MzU4ZDU5OWE4MDcyMzc5NDlkY2JhMzg1ODlhMmFiZTZlYWMxY2Q1ZmQ4MDU4ZmRmNjY4YTc0ODJhN2Q2MTU4NGU0OGM0NDQ3MWU5MyIsImlhdCI6MTY4NDc3NTM3My40MzU1MjEsIm5iZiI6MTY4NDc3NTM3My40MzU1MjUsImV4cCI6MTcwMDY3Mjk3My40MzI1NDYsInN1YiI6IjE3NDA4Iiwic2NvcGVzIjpbXX0.JJYz4M0OYM_xRTxPa5n_wkzcLA7d_rnoElEFElEb6pdiYVKU8mTt7Jxmat5KH2A1aRpgsjELPLs_iKUCFFZ_RpxN0uhzZctTUI-SacQmZyP2nvsRDEzuVjFgGqRdbhJD6zcqQS6gCSx9l1PuYeonCqeFsTCZNgP8mKCT54hWaw0NqQZl_cX75xHqn1bRfkOi7d29N_JB4DhVhIuR2Yt33g0O14kriwiA7_swm-sf_izUiR7NFuwPBdupaWc1WLFa_zCQyYeNlCW2sulX_9v2Qskso1oVuY9eG7ulqA2RPbylc9o_or7QDVu8gOtXaeqyakYbDBeFmIYyWATrU95Dq-EjwqVQYEdIrtCZzAdV0WG1GjPTC_3lOlo-6L8x4U5xx0_n_xxevYFdr1knga8-JmZPRtVTJYsYBuze_7rCY87JVJNyEX0quL0wT0lvF3ZK_K5EZEvjGTnP0c_yJ4cmFT_XDEq2K05WbmLtR-jVo18AFmeBi_ncAyFaCUMHVEzTbTHdA-gmjtXenvD5XX51S8vFOZ5wC3En-U0VqavgOZC8hG2f4Cm6xPdjBZaSyGG0Hz0XEg4896KtN720GG5plruDSZvR1JeU4f0DFWAluWzzVEugKgJxasD0x2CL_lECNReRxxqMdJLp-h8Q0Rh8R0QrBHnSxYcjlWkVErVHDtY',
  'Cookie': 'XSRF-TOKEN=eyJpdiI6ImVPNW5lZnI3d2p5Um5DV25uS0dYdmc9PSIsInZhbHVlIjoiNDh4WWg1dFlDeFBUWlB4RXphTzZkR2laTHFWSm5CT3V1VmVPZDhoTjRFdTFSSzlDWGN1MkwvbVA4T3JDeGlMb3V1SnFGRXIxbEcybUtKWFVOSmNJVXpvcHhXbUI2ZG1MMVB6TUg5N3J2alJFYUJPM3N5dVR1UktTcTdTOTNOS2ciLCJtYWMiOiIzMzE3NmNhNzdhZTMwNDM0MjM5YmJkNzA4ZjZiNGExOGEyMDcwMGExOGIxOTRmMGNkYzNkZDQ3ZGUwNWJmYTBkIiwidGFnIjoiIn0%3D; tspvahan_session=eyJpdiI6ImVEMklSRVhTVjVVRkFiM0tuQVJlaGc9PSIsInZhbHVlIjoiSUY2cStEN0QvdWlhcDNFenBrWU1HU1lDc1djNGwyWktsQ2JySWVFTTZyRzR4KzF6ajlMUVhvQmxBcURSbzJ1ekg5Sk0vR0JmbnpWVjdGWXI5QjZUdUZJaU1LNVpENVdyNTFLSE82dmFXUVBzTit5VWdPamMyMVZvZmpwODltVU8iLCJtYWMiOiI0MGViOTM1Zjc0ZTRmNTVkNWE5N2QzMjc1MzZiNjVmZmJhMjJiM2VlN2ZhYTBlYWZiNzFkZDE0YzEzNmJiODNiIiwidGFnIjoiIn0%3D'
}
vehicle_no='TS09PA3565'
conn.request("POST", "/api/auto-fuel/v1/vehicle/{}".format(vehicle_no), payload, headers)
res = conn.getresponse()
data = res.read()
Data=json.loads(data.decode("utf-8"))
#print(Data)

statusCode=(Data['statusCode'])
messageStatus=(Data['message'])
vehicle_name=(Data['response']['vehicle_name'])
emp_status=(Data['response']['status'])
officer=(Data['response']['officer'])
driver_id=(Data['response']['drivers'][0]['id'])
driver_name=(Data['response']['drivers'][0]['full_name'])
mobile_no=(Data['response']['drivers'][0]['mobile_no'])
fuel_type=(Data['response']['fuel_type'])
current_meter_reading=(Data['response']['current_meter_reading'])
vehicle_unit_name=(Data['response']['vehicle_unit_name'])
vehicle_category=print(Data['response']['vehicle_category'])
vehicle_groups=print(Data['response']['vehicle_groups'])
vehicle_usage_purpose=print(Data['response']['vehicle_usage_purpose'])
regular_quota=(Data['response']['regular_quota'])
additional_quota=(Data['response']['additional_quota'])
total_quota=(Data['response']['total_quota'])
drown=(Data['response']['drown'])
available_quota=(Data['response']['available_quota'])
tank_capacity=(Data['response']['tank_capacity'])


print(vehicle_no,vehicle_name,emp_status,officer,driver_name,fuel_type,total_quota,available_quota,drown,tank_capacity,current_meter_reading,driver_id)



