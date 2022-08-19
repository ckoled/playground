use std::collections::HashMap;
use std::env::args;
use std::fs;
use std::io::stdin;
use std::time::Instant;
use regex::Regex;

fn main() {
    // initialize variables
    let start = Instant::now();
    let mut words = HashMap::new();
    let mut file_path = None;
    let mut top_length = 10;
    let mut target_word = None;
    let mut out_file = None;
    let mut verbose = false;

    // get arguments
    for (i, arg) in args().enumerate() {
        match arg.trim() { 
            "-f" => file_path = args().nth(i+1),
            "-l" => top_length = args().nth(i+1).unwrap().parse().expect("Invalid length"),
            "-w" => target_word = args().nth(i+1),
            "-o" => out_file = args().nth(i+1),
            "-v" => verbose = true,
            _ => ()
        }
    }

    // get file path from stdin or argument
    let file_path = match file_path {
        Some(path) => path,
        None => {
            println!("Enter file name: ");
            let mut buf = String::new();
            if let Err(e) = stdin().read_line(&mut buf) {
                panic!("invalid input, {}", e);
            }
            buf
        }
    };

    // read file and count words
    let re = Regex::new(r#"("|\.|,|\?|!|:|;|_|\(|\))"#).unwrap();
    let file = fs::read_to_string(file_path.trim()).expect("Unable to read file");
    for word in file.split_whitespace() {
        let word = re.replace_all(word, "").into_owned();
        let ent = words.entry(word.to_lowercase()).or_insert(0);
        *ent += 1;
    }
    // println!("{:?}", words);

    // find the top n words
    let mut top_words = vec![(String::new(), 0); top_length];
    match target_word {
        Some(w) => {
            top_words.clear();
            top_words.push((w.clone(), *words.entry(w).or_insert(0)));
        },
        None => {
            for word in words {
                for (i, top) in top_words.iter().enumerate() {
                    if word.1 > top.1 {
                        let mut temp = top_words.drain(i..top_words.len()-1).as_slice().to_vec();
                        top_words[i] = word;
                        top_words.append(&mut temp);
                        break;
                    }
                }
            }
        }
    }

    // print results
    if verbose {
        println!("Rank\tWord           Occurrences");
        for (i, top) in top_words.iter().enumerate() {
            println!("{}\t{:15}{:>11}", i+1, top.0, top.1);
        }
        println!("\n{:?}", start.elapsed());
    }

    if let Some(path) = out_file {
        let mut buf = String::new();
        buf.push_str("Rank,Word,Occurrences\n");
        for (i, top) in top_words.iter().enumerate() {
            buf.push_str(format!("{},{},{}\n", i+1, top.0, top.1).as_str());
        }
        fs::write(path, buf).expect("Unable to write file");
    }
}
