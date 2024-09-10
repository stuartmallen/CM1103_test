import nbformat as nbf
import glob

for f in glob.glob('masters/*.ipynb'):
    print(f)
    nb = nbf.read(f, nbf.NO_CONVERT)

    for c in nb.cells:
        if "# BEGIN NOTE" in c['source']:
            c['source'] = c['source'].split("# BEGIN NOTE")[0] + c['source'].split("# END NOTE")[-1]
        
        if "# NOTE" in c['source']:
            lines = []
            for line in c['source'].split('\n'):
                if "# NOTE" not in line:
                    lines.append(line)
            c['source'] = "\n".join(lines)
    
    nbf.write(nb, f.replace("masters", "student", 1))