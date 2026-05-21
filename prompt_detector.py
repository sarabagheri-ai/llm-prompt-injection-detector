import re

suspicious_patterns = {
    "ignore previous instructions": 3,
    "reveal system prompt": 4,
    "bypass safety": 4,
    "act as administrator": 3,
    "disable restrictions": 3,
    "pretend to be": 2,
    "jailbreak": 5,
    "developer mode": 3
}

def analyze_prompt(prompt):
    prompt_lower = prompt.lower()
    score = 0
    detected = []

    for pattern, risk in suspicious_patterns.items():
        if re.search(pattern, prompt_lower):
            score += risk
            detected.append(pattern)

    if score >= 7:
        level = "HIGH RISK"
    elif score >= 3:
        level = "SUSPICIOUS"
    else:
        level = "SAFE"

    return level, score, detected

if __name__ == "__main__":
    user_prompt = input("Enter prompt: ")

    level, score, detected = analyze_prompt(user_prompt)

    print("\n=== Analysis Result ===")
    print(f"Risk Level: {level}")
    print(f"Risk Score: {score}")

    if detected:
        print("Detected Patterns:")
        for item in detected:
            print(f"- {item}")
    else:
        print("No suspicious patterns detected.")
