import random

# Existing letters 11-20
existing_letters = [
  {
    "id": 11,
    "title": "Letter #11",
    "content": """
      <p>My love,</p>
      <p>
          Today I just want you to know that loving you feels effortless. It doesn’t feel forced or dramatic —
          it feels natural, like breathing. You’ve become my favorite part of every single day.
      </p>
      <p>
          Thank you for being exactly who you are. I wouldn’t change a single thing about you.
      </p>
      <p>Forever yours,</p>
      <p><strong>Tu negrito</strong></p>
    """
  },
  {
    "id": 12,
    "title": "Letter #12",
    "content": """
      <p>Beautiful,</p>
      <p>
          You have this quiet power over my heart. A smile from you can change my entire mood. A hug from you
          can reset my whole world. That’s not exaggeration — that’s truth.
      </p>
      <p>
          I am so grateful that I get to love you and call you mine.
      </p>
      <p>With all my heart,</p>
      <p><strong>Tu negrito</strong></p>
    """
  },
  {
    "id": 13,
    "title": "Letter #13",
    "content": """
      <p>My favorite person,</p>
      <p>
          If someone asked me what happiness looks like, I would describe a moment with you —
          laughing about something small, talking about nothing, just existing side by side.
      </p>
      <p>
          You make ordinary moments feel extraordinary.
      </p>
      <p>Love always,</p>
      <p><strong>Tu negrito</strong></p>
    """
  },
  {
    "id": 14,
    "title": "Letter #14",
    "content": """
      <p>My heart,</p>
      <p>
          I admire you more than you probably realize. Your strength, your kindness, your determination —
          they inspire me every single day.
      </p>
      <p>
          Loving you isn’t just about romance. It’s about respect. It’s about partnership. It’s about choosing
          each other again and again.
      </p>
      <p>Always choosing you,</p>
      <p><strong>Tu negrito</strong></p>
    """
  },
  {
    "id": 15,
    "title": "Letter #15",
    "content": """
      <p>My love,</p>
      <p>
          I never want you to doubt how deeply you matter to me. You are not just someone I love —
          you are someone I value, someone I cherish, someone I protect.
      </p>
      <p>
          My heart feels safe with you, and that’s one of the greatest gifts I’ve ever received.
      </p>
      <p>Forever grateful,</p>
      <p><strong>Tu negrito</strong></p>
    """
  },
  {
    "id": 16,
    "title": "Letter #16",
    "content": """
      <p>Sweetheart,</p>
      <p>
          There are so many little things about you that I adore — the way you look at me when I’m talking,
          the way you laugh when something genuinely surprises you, the way you care so deeply.
      </p>
      <p>
          Those small details are everything to me.
      </p>
      <p>With love,</p>
      <p><strong>Tu negrito</strong></p>
    """
  },
  {
    "id": 17,
    "title": "Letter #17",
    "content": """
      <p>My love,</p>
      <p>
          You make my world softer. Calmer. Warmer. You’ve become the place I go when I need peace,
          and the person I go to when I need strength.
      </p>
      <p>
          I don’t just love you — I trust you. And that means everything.
      </p>
      <p>Always yours,</p>
      <p><strong>Tu negrito</strong></p>
    """
  },
  {
    "id": 18,
    "title": "Letter #18",
    "content": """
      <p>Beautiful soul,</p>
      <p>
          Loving you feels like building something real. Something steady. Something lasting.
          Not just butterflies — but foundation.
      </p>
      <p>
          I am so proud of the love we share.
      </p>
      <p>With all that I am,</p>
      <p><strong>Tu negrito</strong></p>
    """
  },
  {
    "id": 19,
    "title": "Letter #19",
    "content": """
      <p>My heart,</p>
      <p>
          If I could pause time, I’d freeze it during one of our quiet moments —
          just us, no noise, no rush. Because those are the moments I feel it most:
          how deeply connected we are.
      </p>
      <p>
          Thank you for being my constant.
      </p>
      <p>Yours always,</p>
      <p><strong>Tu negrito</strong></p>
    """
  },
  {
    "id": 20,
    "title": "Letter #20",
    "content": """
      <p>My love,</p>
      <p>
          I hope you never forget how special you are to me. You are not just part of my life —
          you are woven into it. Into my thoughts, my plans, my dreams.
      </p>
      <p>
          This Valentine’s project is just a small reflection of a very big love.
      </p>
      <p>Forever and always,</p>
      <p><strong>Tu negrito</strong></p>
    """
  }
]

# Components for new letters
salutations = [
    "My love,", "Sweetheart,", "My dearest,", "Beautiful,", "My angel,", "To my soulmate,",
    "My everything,", "Darling,", "My heart,", "To the one I love,"
]

openers = [
    "Every day with you is a gift I cherish.",
    "I was just thinking about how lucky I am to have you.",
    "You are the best thing that ever happened to me.",
    "My life is infinitely better because you are in it.",
    "I love you more than words can say.",
    "You make my heart smile in ways no one else can.",
    "Thinking of you makes my day brighter.",
    "Loving you is the easiest thing I've ever done.",
    "You are my dream come true.",
    "I fall in love with you more every single day."
]

bodies = [
    "Your smile lights up my world, and your laugh is my favorite sound. I promise to always be by your side, through every high and every low.",
    "I appreciate you more than you know. Your kindness, your strength, and your beauty amaze me constantly.",
    "No matter where life takes us, I want you to know that you are my home. I find peace in your arms and joy in your presence.",
    "You inspire me to be a better person. Thank you for believing in me and for loving me exactly as I am.",
    "I cherish every moment we spend together, from the quiet ones to the crazy ones. You are my partner in everything.",
    "I wish I could show you how much you mean to me. You are the center of my universe and the beat of my heart.",
    "I love the life we are building together. There is no one else I would rather share this journey with.",
    "You are my best friend and my greatest love. I can't wait for all the memories we have yet to make.",
    "Just wanted to remind you that you are beautiful, capable, and deeply loved. Never forget that.",
    "My love for you grows stronger with each passing moment. You are my forever."
]

closings = [
    "Yours forever,",
    "With all my love,",
    "Forever and always,",
    "Love you endlessly,",
    "Always yours,",
    "With all my heart,",
    "Eternally yours,",
    "Loving you always,",
    "Yours truly,"
]

# Generate 200 letters
new_letters = []
for i in range(200):
    letter_id = 21 + i
    salutation = random.choice(salutations)
    opener = random.choice(openers)
    body = random.choice(bodies)
    closing = random.choice(closings)
    
    content = f"""
      <p>{salutation}</p>
      <p>
          {opener} {body}
      </p>
      <p>{closing}</p>
      <p><strong>Tu negrito</strong></p>
    """
    
    new_letters.append({
        "id": letter_id,
        "title": f"Letter #{letter_id}",
        "content": content
    })

all_letters = existing_letters + new_letters

# Write to JS file
js_content = "const loveLetters = [\n"
for letter in all_letters:
    js_content += "  {\n"
    js_content += f"    id: {letter['id']},\n"
    js_content += f"    title: \"{letter['title']}\",\n"
    js_content += f"    content: `{letter['content']}`\n"
    js_content += "  },\n"
js_content += "];\n\nexport default loveLetters;\n"

with open(r"c:\Users\idiel\Desktop\Repos\my-valentine\src\assets\loveLetters.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Successfully generated loveLetters.js with 210 letters.")
