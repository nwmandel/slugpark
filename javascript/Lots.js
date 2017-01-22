// Group: SlugPark
// HackUCSC 2017

class Lot {
	constructor(spaces, filled = 0) {
		this.spaces = spaces;
		this.filled = filled;
	}

	// Return the number of total spaces and taken spaces
	getSpaces() {
		return this.spaces;
	}
	getFilled() {
		return this.filled;
	}

	// Change the number of cars in the lot
	set filled(f) {
		this.filled = f;
	}

	calcFull() {
		return this.filled == this.spaces;
	}

	calcEmpty() {
		return this.filled == 0;
	}
	
}