-- Per-workspace CompetiTest overrides for CSES.
-- Global defaults live in ~/.config/nvim/lua/plugins/competitest.lua.
return {
  -- When you use `:CompetiTest receive problem` (Competitive Companion creates
  -- the source file for you), start it from these templates:
  template_file = {
    [".cpp"] = "~/Desktop/cses/template.cpp",
    [".py"] = "~/Desktop/cses/template.py",
    [".rs"] = "~/Desktop/cses/template.rs",
    [".java"] = "~/Desktop/cses/Main.java",
  },
  evaluate_template_modifiers = true,
}
