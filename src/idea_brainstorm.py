import argparse, json
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv; load_dotenv()
import jsonschema
from jsonschema import validate
from datetime import datetime

SCHEMA = {
  "type":"object",
  "properties":{
    "ideas":{"type":"array","items":{
      "type":"object",
      "properties":{
        "title":{"type":"string"},
        "problem":{"type":"string"},
        "impact":{"type":"integer","minimum":1,"maximum":10},
        "effort":{"type":"integer","minimum":1,"maximum":10}
      },
      "required":["title","problem","impact","effort"]
    }}
  },
  "required":["ideas"]
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("topic", nargs="+", help="Topic to ideate on")
    args = parser.parse_args()
    topic = " ".join(args.topic)

    client = OpenAI()
    prompt = f"""Generate 5 product ideas for: {topic}.
Return ONLY valid JSON matching:
{{"ideas":[{{"title":"...","problem":"...","impact":1-10,"effort":1-10}}]}}"""

    r = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type":"json_object"},
        messages=[{"role":"user","content": prompt}],
        temperature=0.3
    )
    data = json.loads(r.choices[0].message.content)
    validate(instance=data, schema=SCHEMA)

    outdir = Path("data/outputs"); outdir.mkdir(parents=True, exist_ok=True)
    fname = outdir / f"ideas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    fname.write_text(json.dumps(data, indent=2))
    print(f"Saved ideas to {fname}")

if __name__ == "__main__":
    main()
