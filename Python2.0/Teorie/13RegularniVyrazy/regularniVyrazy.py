import re

text = "Email pana Kolika je kolik@email.com.\nTento email nemá pan Kolík již 5 let."

# Nalezení emailové adresy
email_vzor = r"([a-z\d]+[a-z\d\.-_]*[a-z0-9]+)@(\w+.\w{2,3})"
emaily = re.findall(email_vzor, text)
print(f"Nalezené emaily: {emaily}")

# Rozdělení textu
casti = re.split(r"\.", text)
print(f"Rozdělený text: {casti}")

# Nahrazení textu
novy_text = re.sub(r"[kK]ol[ií]k", "Ladan", text)
print(f"Záměna kolik za Ladan: {novy_text}")