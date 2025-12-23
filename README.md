# Sudoku Solver with Pygame Visualization

A visual Sudoku solver using the **Backtracking Algorithm** with real-time pygame animation. Watch as the algorithm solves puzzles step-by-step, showing every number placement and backtrack decision.

## 🎯 Features

- **4x4 Sudoku Solver** (`fourfour.py`) - Solves small puzzles quickly
- **8x8 Sudoku Solver** (`eighttoeight.py`) - Solves larger puzzles
- **Real-time Visualization** - Watch the algorithm work in action
- **Detailed Statistics** - Track attempts and backtracks
- **Color-coded Display**:
  - **Black numbers** = Given/initial clues
  - **Green numbers** = Numbers solved by the algorithm
  - **Yellow highlight** = Current cell being processed
  - **Red highlight** = Backtracking (removing invalid number)
- **Interactive Window** - Close anytime with window close button

## 📋 Requirements

- Python 3.6+
- pygame

## 🚀 Installation

1. **Install pygame** if you haven't already:
```bash
pip install pygame
```

2. **Navigate to the project directory**:
```bash
cd "Random project"
```

## 🎮 How to Use

### Run the 4x4 Solver:
```bash
python fourfour.py
```

### Run the 8x8 Solver:
```bash
python eighttoeight.py
```

The program will:
1. Display the initial puzzle
2. Start solving with animated steps
3. Show the final solved puzzle
4. Print statistics to the console
5. Keep the window open for viewing (close to exit)

## 📊 Understanding the Visualization

### Info Panel (Bottom of Window)
- **Attempts**: Total number of tries to place a number
- **Backtracks**: Number of times the algorithm had to remove an invalid number and try another
- **Cell Status**: Current cell being processed and what number is being tried

### Color Legend
| Color | Meaning |
|-------|---------|
| Black Text | Given number (initial puzzle) |
| Green Text | Solved by algorithm |
| Yellow Background | Cell being tested |
| Red Background | Backtracking in progress |

### Grid Lines
- **Thin lines** = Individual cells (1 cell)
- **Thick lines** = Subgrid boxes (2x2 for 4x4, 3x3 for 8x8)

## 🧠 How the Backtracking Algorithm Works

1. **Find empty cell**: Scans the board for the next empty cell (0)
2. **Try numbers**: Attempts to place each valid number (1-4 for 4x4, 1-9 for 8x8)
3. **Validate**: Checks if the number violates Sudoku rules:
   - Not already in the same row
   - Not already in the same column
   - Not already in the same subgrid
4. **Recurse**: If valid, moves to the next empty cell
5. **Backtrack**: If no valid number works, removes the last placed number and tries the next option
6. **Success**: When all cells are filled without conflicts, puzzle is solved

### Example Flow:
```
[Empty Cell]
├─ Try 1 → Valid? 
│  ├─ Move to next cell
│  │  ├─ Try 1 → Invalid (already in row)
│  │  ├─ Try 2 → Valid
│  │  │  ├─ Eventually hit dead end
│  │  │  └─ BACKTRACK: Remove 2
│  │  ├─ Try 3 → Valid... [continues]
│  │  └─ Try 4 → Valid... [continues]
│  └─ If all branches fail, BACKTRACK: Remove 1
├─ Try 2 → Valid?
├─ Try 3 → Valid?
└─ Try 4 → Valid?
```

## 📁 File Descriptions

### `fourfour.py`
- **Type**: 4x4 Sudoku solver
- **Puzzle Size**: 4 cells per row/column
- **Subgrid Size**: 2x2 blocks
- **Numbers Used**: 1-4
- **Best for**: Quick demonstrations, learning the algorithm

### `eighttoeight.py`
- **Type**: 8x8 Sudoku solver
- **Puzzle Size**: 8 cells per row/column
- **Subgrid Size**: 2x4 blocks (or 4x2)
- **Numbers Used**: 1-8
- **Best for**: More complex puzzles, real-world examples

### `README.md`
- This file - documentation and usage guide

## 💡 Key Metrics

When the program completes, it shows:
- **Attempts**: How many placements were tried (including invalid ones)
- **Backtracks**: How many times the algorithm had to undo a placement

**Example Output**:
```
✓ Total attempts to place numbers: 45
✓ Total backtracks (failed attempts): 12
```

Lower backtracks = more efficient solving path

## 🎓 Educational Value

This project demonstrates:
- **Recursive Backtracking** algorithm
- **Constraint Satisfaction Problems (CSP)**
- **Data Visualization** with pygame
- **Algorithm Animation** for better understanding
- **Real-time Statistics** tracking

## 🔧 Customization

### Change the puzzle:
Edit the `board` variable in the code:
```python
board = [
    [1, 0, 0, 4],
    [0, 0, 3, 0],
    [0, 3, 0, 0],
    [2, 0, 0, 1]
]
```
Replace `0` with numbers for clues, keep `0` for empty cells.

### Adjust animation speed:
Find the `clock.tick()` lines and change the value (higher = faster):
```python
clock.tick(10)  # 10 FPS - slow and clear
# or
clock.tick(30)  # 30 FPS - faster
```

### Change colors:
Modify the color definitions at the top of the file:
```python
LIGHT_YELLOW = (255, 255, 200)  # RGB values
RED = (255, 100, 100)
```

## ⚠️ Troubleshooting

**"pygame not found"**
```bash
pip install pygame
```

**Window is frozen**
- The algorithm is still solving (can take a few seconds for 8x8)
- Wait for it to complete

**Program runs very slowly**
- Reduce the `clock.tick()` value to increase FPS
- Or modify the update frequency in the solve function

## 📝 Notes

- The 4x4 solver typically completes in under 1 second
- The 8x8 solver may take 5-30 seconds depending on puzzle difficulty
- The number of backtracks varies greatly based on the initial puzzle configuration
- Some puzzles may require thousands of attempts

## 🎯 Future Enhancements

Potential improvements:
- [ ] Load puzzles from files
- [ ] Add difficulty levels
- [ ] Implement optimized solving strategies (constraint propagation)
- [ ] Save solved puzzles
- [ ] Multiple solving algorithm options
- [ ] Speed controls via keyboard

## 📄 License

Free to use and modify for educational purposes.

---

**Made with ❤️ for learning backtracking algorithms**

Enjoy watching your puzzles get solved! 🎮
