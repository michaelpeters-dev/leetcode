# CSES local workflow

One-time setup and the do → test → submit loop for CSES problems in neovim.

## One-time setup

1. **Log in to CSES** (opens a browser link, paste the code back):
   ```sh
   cses-cli login
   cses-cli status      # confirm you're logged in
   ```
2. **(Optional) Competitive Companion browser extension** — Chrome/Firefox.
   This is what makes `<leader>ct` pull sample tests in one click.

## The loop

### 1. Start a problem
Copy the template, naming the file by the **CSES task id** (find it in the URL:
`cses.fi/problemset/task/1068` → task id `1068`):
```sh
cp template.cpp 1068.cpp        # or template.py / template.rs
nvim 1068.cpp
```
> Java: make a sub-folder and use `Main.java` (see note in `Main.java`).

### 2. Get the sample tests
- **Browser:** open the problem page, click the Competitive Companion "+" button,
  then in nvim press `<leader>ct` (`:CompetiTest receive testcases`).
- **Terminal only:** `cses-cli samples -c problemset -t 1068 .`
  (writes `1.in`, `1.out`, …), or add cases by hand with `<leader>ca`.
- **Read the statement:** `cses-cli view -c problemset -t 1068`

### 3. Test locally
In nvim: `<leader>cr` (`:CompetiTest run`) — compiles and runs against every
sample, showing a pass/fail diff. `R` re-runs, `d` toggles the diff, `q` closes.

### 4. Submit
- **In nvim:** `<leader>cs` → type the task id → runs `cses-cli submit` in a split.
- **Terminal:** `cses-cli submit 1068.cpp -c problemset -t 1068`
  - `-o C++20` to force a compiler option; otherwise the server auto-detects.
  - `cses-cli submission -t 1068` shows the latest verdict.

## CompetiTest keymaps (leader = space)
| Key | Action |
|-----|--------|
| `<leader>cr` | Run against all sample tests |
| `<leader>ct` | Receive tests from Competitive Companion |
| `<leader>ca` | Add a test case by hand |
| `<leader>ce` | Edit a test case |
| `<leader>cd` | Delete a test case |
| `<leader>cs` | Submit current file to CSES |

## Notes
- Tests are stored next to the source as `<name>.testcases` (e.g. `1068.testcases`).
- C++ compiles with `g++` (Apple Clang) using your `~/programming/cpp/include`
  `bits/stdc++.h` shim via `CPATH` — same as your existing setup.
- The course id for the CSES Problem Set is `problemset`; `cses-cli` remembers
  `-c` after the first use, so you can drop it later.
