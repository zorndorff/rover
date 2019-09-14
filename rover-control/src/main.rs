#![feature(proc_macro_hygiene, decl_macro)]
extern crate actix;
extern crate sysfs_gpio;

mod server;

fn main() {
    let system = actix::System::new("PiBot");
    system.run();
}