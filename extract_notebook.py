import json
import sys
import io

# Set stdout to handle Unicode properly
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('src/FMTS_v2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print(f'Total cells: {len(nb.get("cells", []))}')
print('\n' + '='*80)

cell_count = 0
for i, cell in enumerate(nb.get('cells', [])):
    if cell['cell_type'] == 'code':
        outputs = cell.get('outputs', [])
        if outputs:
            cell_count += 1
            source_lines = cell.get('source', [])
            source_text = ''.join(source_lines) if isinstance(source_lines, list) else source_lines
            
            print(f'\nCELL {i} (Code Cell)')
            if len(source_text) > 100:
                print(f'Source: {source_text[:100]}...')
            else:
                print(f'Source: {source_text.strip()}')
            print('-' * 80)
            
            for out_idx, output in enumerate(outputs):
                out_type = output.get('output_type', 'unknown')
                
                if out_type == 'stream':
                    text = ''.join(output.get('text', []))
                    print(f'[Stream]:\n{text}')
                    
                elif out_type == 'execute_result':
                    data = output.get('data', {})
                    if 'text/plain' in data:
                        text_output = data['text/plain']
                        if isinstance(text_output, list):
                            text_output = ''.join(text_output)
                        print(f'[Result]:\n{text_output}')
                        
                elif out_type == 'display_data':
                    data = output.get('data', {})
                    if 'text/plain' in data:
                        text_output = data['text/plain']
                        if isinstance(text_output, list):
                            text_output = ''.join(text_output)
                        print(f'[Display]:\n{text_output}')
                        
                elif out_type == 'error':
                    ename = output.get('ename', 'Unknown')
                    evalue = output.get('evalue', '')
                    print(f'[ERROR: {ename}] {evalue}')
            
            print('='*80)

print(f'\n\nTotal cells with outputs: {cell_count}')
