# Let's define rule-based filters, this can be extended with time.
import re

def is_phishing_sms(sms_text):
    """
    Checks if an SMS matches phishing criteria based on defined rules.
    Returns True if the SMS is flagged as phishing, otherwise False.
    """
    if contains_suspicious_link(sms_text):
        return True
    if contains_suspicious_keywords(sms_text):
        return True
    if uses_time_pressure(sms_text):
        return True
    if contains_fake_authority_claims(sms_text):
        return True
    if has_unusual_formatting(sms_text):
        return True
    if comes_from_foreign_number(sms_text):
        return True
    if contains_fake_login_links(sms_text):
        return True
    if contains_generic_greetings(sms_text):
        return True
    return False

def get_rule_violated(sms_text):
    """
    Checks which rule was violated for phishing SMS detection.
    Returns a description of the rule violated or 'No rule violated' if none.
    """
    if contains_suspicious_link(sms_text):
        return "Contains a suspicious link."
    if contains_suspicious_keywords(sms_text):
        return "Contains suspicious keywords commonly used in phishing messages."
    if uses_time_pressure(sms_text):
        return "Contains urgency phrases to pressure the recipient into acting quickly."
    if contains_fake_authority_claims(sms_text):
        return "Contains fake claims of authority to scare the recipient."
    if has_unusual_formatting(sms_text):
        return "Has unusual formatting (e.g., excessive capitalization or punctuation)."
    if comes_from_foreign_number(sms_text):
        return "Appears to come from a foreign number, which is unusual."
    if contains_fake_login_links(sms_text):
        return "Contains fake login links resembling legitimate domains."
    if contains_generic_greetings(sms_text):
        return "Uses generic greetings, which are often used in mass phishing attempts."
    return "No rule violated."


# Rule 1: Suspicious Links
def contains_suspicious_link(sms_text):
    pattern = r"(http|https|www)\S+"
    if re.search(pattern, sms_text):
        return True
    return False

# Rule 2: Suspicious Keywords
def contains_suspicious_keywords(sms_text):
    keywords = [
        "kazan", "çevrimsiz", "hemen tıkla", "acil tıkla",
        "hemen üye ol", "boş yok", "promosyon kazan",
        "çekiliş kazandınız", "ödül kazandınız", "son şans",
        "araba kazandınız", "Tebrikler ödül kazandınız",
    ]
    for keyword in keywords:
        if keyword.lower() in sms_text.lower():
            return True
    return False

# Rule 3: Time Pressure
def uses_time_pressure(sms_text):
    urgency_phrases = [
        "bugün içinde işlem yapın", "son 1 saat", "son gün",
        "hesabınız kapatılacak", "hemen tıkla", "çevrimsiz", "hemen kazan"
    ]
    for phrase in urgency_phrases:
        if phrase.lower() in sms_text.lower():
            return True
    return False


# Rule 4: Fake Authority Claims
def contains_fake_authority_claims(sms_text):
    authority_phrases = [
        "adınıza açılmış bir dava var",
        "polis tarafından aranıyorsunuz",
        "vergi borcunuz var",
        "sgk ödemesi",
        "maaşınız bloke edildi"
    ]
    for phrase in authority_phrases:
        if phrase.lower() in sms_text.lower():
            return True
    return False


# Rule 5: Unusual Formatting
def has_unusual_formatting(sms_text):
    if re.search(r"[A-Z]{5,}", sms_text):  # Excessive capitalization
        return True
    if re.search(r"[!]{3,}", sms_text):  # Excessive exclamation marks
        return True
    if re.search(r"\.\.\.", sms_text):  # Multiple ellipses
        return True
    return False


# Rule 6: Foreign Number
def comes_from_foreign_number(sms_text, sender_number="+90"):
    # Placeholder sender_number, update logic to verify the actual sender
    if not sender_number.startswith("+90"):
        return True
    return False


# Rule 7: Fake Login Links
def contains_fake_login_links(sms_text):
    phishing_domains = [
        "ziraaatbank.com", "paypa1.com", "turktelekomi.com"
    ]
    for domain in phishing_domains:
        if domain in sms_text:
            return True
    return False


# Rule 8: Generic Greetings
def contains_generic_greetings(sms_text):
    greetings = ["sayın müşteri", "değerli kullanıcı", "sevgili müşteri"]
    for greeting in greetings:
        if greeting.lower() in sms_text.lower():
            return True
    return False
