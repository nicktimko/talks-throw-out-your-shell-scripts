import subprocess
import sys
import tempfile


def main():
    with tempfile.NamedTemporaryFile(mode="w+") as tf:
        tf.write("\n\n# Enter a message!\n")
        tf.seek(0)

        # let the user use a real text editor
        proc = subprocess.run(["vim", tf.name])

        for line in tf:
            if line.lstrip().startswith("#"):
                continue
            print("--> ", line, end="")


if __name__ == "__main__":
    sys.exit(main())
