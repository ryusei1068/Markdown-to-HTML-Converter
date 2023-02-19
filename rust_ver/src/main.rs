use std::env;
use std::fs;
use text_colorizer::*;

#[derive(Debug)]
struct Arguments {
    inputfile: String,
    outputfile: String,
}

fn parse_args() -> Arguments {
    let args: Vec<String> = env::args().skip(1).collect();

    if args.len() != 3 {
        eprintln!(
            "{} wrong number of arguments: expected 3, got {}.",
            "Error:".red().bold(),
            args.len()
        );
        std::process::exit(1);
    }

    Arguments {
        inputfile: args[1].clone(),
        outputfile: args[2].clone(),
    }
}

fn main() {
    let args = parse_args();

    let data = match fs::read_to_string(&args.inputfile) {
        Ok(v) => v,
        Err(e) => {
            eprintln!(
                "{} failed to read from file '{}': {:?}",
                "Error:".red().bold(),
                args.inputfile,
                e
            );
            std::process::exit(1);
        }
    };

    let parser = pulldown_cmark::Parser::new(&data);
    let mut html_output = String::new();
    pulldown_cmark::html::push_html(&mut html_output, parser);

    match fs::write(&args.outputfile, html_output.clone()) {
        Ok(v) => v,
        Err(e) => {
            eprintln!(
                "{} failed to write to file '{}': {:?}",
                "Error:".red().bold(),
                args.outputfile,
                e
            );
            std::process::exit(1);
        }
    }
}
