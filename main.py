from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def check_fansale_tickets_selenium(url):
    # Headless Modus
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')  # Wenn du im Headless-Modus arbeiten möchtest, kannst du das aktivieren
    driver = webdriver.Chrome(options=options)
    
    # Rufe die Seite auf
    driver.get(url)
    
    # Warte ein paar Sekunden, damit die Seite vollständig geladen wird
    time.sleep(8)  # Das kann je nach Verbindung und Ladegeschwindigkeit angepasst werden
    
    # Versuche, das Ticket-Element zu finden
    try:
        tickets_section = driver.find_element(By.ID, 'fansaleEvents')
        
        # Finde alle Event-Einträge
        event_entries = tickets_section.find_elements(By.CLASS_NAME, 'EvEntry')
        
        if event_entries:
            # Falls Tickets vorhanden sind, gib die relevanten Informationen aus
            for event in event_entries:
                title = event.get_attribute('aria-label')
                price_element = event.find_element(By.CLASS_NAME, 'EvEntryRow-moneyValueFormat')
                price = price_element.text if price_element else 'Unbekannt'
                
                print(f"Event: {title}")
                print(f"Preis: {price}")
                print(f"Link: {event.get_attribute('href')}")
                print("-" * 40)
        else:
            print("Keine Tickets im Fansale gefunden.")
    
    except Exception as e:
        print("Keine Tickets im Fansale verfügbar.")
        
        # Suche nach der Eventim-Box
        try:
            eventim_box = driver.find_element(By.CLASS_NAME, 'js-EventimEvents')
            if eventim_box:
                print("Es gibt noch Tickets auf Eventim, aber nicht im Fansale.")
        except Exception as e2:
            print("Weder Fansale-Tickets noch Eventim-Tickets verfügbar.")
    
    # Schließe den Browser
    driver.quit()

# Beispiel-URL
url = 'https://www.fansale.de/tickets/all/rock-am-ring/538'
check_fansale_tickets_selenium(url)
