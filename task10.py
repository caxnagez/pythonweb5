import argparse
import textwrap

def format_text_block(frame_height, frame_width, file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return str(e)

    # Разбиваем текст на строки и обрезаем по ширине
    lines = content.splitlines()
    wrapped_lines = []
    for line in lines:
        if len(line) <= frame_width:
            wrapped_lines.append(line)
        else:
            wrapped_lines.extend(textwrap.wrap(line, width=frame_width))

    # Обрезаем по высоте
    final_lines = wrapped_lines[:frame_height]

    return "\n".join(final_lines)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--frame-height', type=int, required=True)
    parser.add_argument('--frame-width', type=int, required=True)
    parser.add_argument('file_name', type=str)
    args = parser.parse_args()

    result = format_text_block(args.frame_height, args.frame_width, args.file_name)
    print(result)

if __name__ == "__main__":
    main()