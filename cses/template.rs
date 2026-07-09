use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();

    let stdout = io::stdout();
    let mut out = io::BufWriter::new(stdout.lock());

    // Grab the next whitespace-separated token and parse it:
    //   let n: usize = tokens.next().unwrap().parse().unwrap();

    let _ = &mut tokens;
    writeln!(out).ok();
}
