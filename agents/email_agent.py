def generate_email_response(email_text, tone):

    if tone.lower() == "professional":
        return f"""Dear Sir/Madam,

Thank you for your email regarding:

"{email_text}"

I will get back to you shortly.

Best regards,
Your Name"""

    elif tone.lower() == "friendly":
        return f"""Hi there 😊

Thanks for your message about:

"{email_text}"

I'll look into it soon!

Cheers,
Your Name"""

    else:
        return f"""Thank you for your message:

"{email_text}"

I will respond shortly."""