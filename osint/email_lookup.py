# Herramienta educativa OSINT - Solo para consultar fuentes públicas
import requests

def check_email_breaches(email):
    """Verifica si un email aparece en filtraciones públicas (API de Have I Been Pwned)"""
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"hibp-api-key": "DEMO_KEY"}  # Reemplazar con key real para uso serio
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print(f"⚠️ El email {email} apareció en filtraciones.")
    elif response.status_code == 404:
        print(f"✅ El email {email} no está en filtraciones conocidas.")
    else:
        print("🔒 Uso educativo: necesitas API key para consultas reales.")

if __name__ == "__main__":
    email = input("Correo a verificar (educativo): ")
    check_email_breaches(email)
