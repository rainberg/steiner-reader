#!/usr/bin/env python3
"""Download all GA PDFs from bdn-steiner.ru"""
import subprocess
import os
import time
import json
from pathlib import Path

# All GA IDs we have in our database
ga_ids = [
    "001","002","003","004","004a","005","006","007","008","009",
    "010","011","012","013","014","015","016","017","018","019",
    "020","021","022","023","024","025","026","027","028","029",
    "030","031","032","033","034","035","036","037","038","039",
    "040","040a","041","042","043","044","045","046","047","048",
    "049","050","051","052","053","054","055","056","057","058",
    "059","060","061","062","063","064","065","066","067","068",
    "069a","069b","069c","069d","069e","070","071","072","073","073a",
    "074","075","076","077a","077b","078","079","080","081","082",
    "083","084","085","086","087","088","089","090","091","092",
    "093","094","095","096","097","098","099","100","101","102",
    "103","104","105","106","107","108","109","110","111","112",
    "113","114","115","116","117","118","119","120","121","122",
    "123","124","125","126","127","128","129","130","131","132",
    "133","134","135","136","137","138","139","140","141","142",
    "143","144","145","146","147","148","149","150","151","152",
    "153","154","155","156","157","158","159","160","161","162",
    "163","164","165","166","167","168","169","170","171","172",
    "173","174","175","176a","176b","177","178","179","180","181",
    "182","183","184","185","186","187","188","189","190","191",
    "192","193","194","195","196","197","198","199","200","201",
    "202","203","204","205","206","207","208","209","210","211",
    "212","213","214","215","216","217","218","219","220","221",
    "222","223","224","225","226","227","228","229","230","231",
    "232","233","234","235","236","237","238","239","240","241",
    "242","243","244","245","246","247","248","249","250","251",
    "252","253","254","255","256","257","258","259","260","261",
    "262","263","264","265","266","267","268","269","270","271",
    "272","273","274","275","276","277","278","279","280","281",
    "282","283","284","285","286","287","288","289","290","291",
    "292","293","294","295","296","297","298","299","300","301",
    "302","303","304","305","306","307","308","309","310","311",
    "312","313","314","315","316","317","318","319","320","321",
    "322","323","324","325","326","327","328","329","330","331",
    "332","333","334","335","336","337","338","339","340","341",
    "342","343","344","345","346","347","348","349","350","351","352"
]

pdf_dir = Path.home() / "steiner-reader" / "data" / "pdf"
pdf_dir.mkdir(parents=True, exist_ok=True)

results = {"success": [], "not_found": [], "failed": [], "skipped": []}

for i, ga_id in enumerate(ga_ids):
    filename = f"GA{ga_id.upper()}.pdf"
    filepath = pdf_dir / filename
    
    # Skip if already downloaded and > 100KB
    if filepath.exists() and filepath.stat().st_size > 100000:
        results["skipped"].append(ga_id)
        continue
    
    url = f"http://bdn-steiner.ru/cat/ga/{ga_id}.pdf"
    
    try:
        result = subprocess.run(
            ["curl", "-s", "-f", "-o", str(filepath), "-w", "%{http_code}", 
             "--connect-timeout", "15", "--max-time", "120", url],
            capture_output=True, text=True, timeout=130
        )
        
        if result.stdout == "200":
            size = filepath.stat().st_size
            if size > 1000:  # At least 1KB
                results["success"].append({"id": ga_id, "size": size})
                print(f"[{i+1}/{len(ga_ids)}] OK GA{ga_id} ({size//1024}KB)")
            else:
                filepath.unlink(missing_ok=True)
                results["not_found"].append(ga_id)
                print(f"[{i+1}/{len(ga_ids)}] SKIP GA{ga_id} (too small)")
        else:
            results["not_found"].append(ga_id)
            filepath.unlink(missing_ok=True)
            print(f"[{i+1}/{len(ga_ids)}] MISS GA{ga_id} (HTTP {result.stdout})")
    except Exception as e:
        results["failed"].append({"id": ga_id, "error": str(e)})
        print(f"[{i+1}/{len(ga_ids)}] ERR GA{ga_id}: {e}")
    
    # Small delay to be polite
    time.sleep(0.5)

# Summary
print(f"\n{'='*50}")
print(f"Success: {len(results['success'])}")
print(f"Not found: {len(results['not_found'])}")
print(f"Failed: {len(results['failed'])}")
print(f"Skipped: {len(results['skipped'])}")
print(f"Total size: {sum(r['size'] for r in results['success']) // (1024*1024)}MB")

# Save results
with open(pdf_dir / "download_results.json", "w") as f:
    json.dump(results, f, indent=2)
