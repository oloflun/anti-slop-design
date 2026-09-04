// React Theme — extracted from https://springsummer.dk/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '10': string;
    '12': string;
    '14': string;
    '18': string;
    '20': string;
    '25': string;
    '331.84': string;
    '146.4': string;
    '38.4': string;
    '13.3333': string;
 *   };
 *   space: {
    '2': string;
    '18': string;
    '30': string;
    '40': string;
    '50': string;
    '60': string;
    '80': string;
    '100': string;
    '150': string;
    '250': string;
 *   };
 *   radii: {
    sm: string;
    full: string;
 *   };
 *   shadows: {

 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "primary": "#fe3939",
    "background": "#dedcd3",
    "foreground": "#000000",
    "neutral50": "#ffffff",
    "neutral100": "#000000",
    "neutral200": "#dedcd3"
  },
  "fonts": {
    "body": "'Grotesk', sans-serif"
  },
  "fontSizes": {
    "10": "10px",
    "12": "12px",
    "14": "14px",
    "18": "18px",
    "20": "20px",
    "25": "25px",
    "331.84": "331.84px",
    "146.4": "146.4px",
    "38.4": "38.4px",
    "13.3333": "13.3333px"
  },
  "space": {
    "2": "2px",
    "18": "18px",
    "30": "30px",
    "40": "40px",
    "50": "50px",
    "60": "60px",
    "80": "80px",
    "100": "100px",
    "150": "150px",
    "250": "250px"
  },
  "radii": {
    "sm": "3px",
    "full": "50px"
  },
  "shadows": {},
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "primary": {
      "main": "#fe3939",
      "light": "hsl(0, 99%, 76%)",
      "dark": "hsl(0, 99%, 46%)"
    },
    "background": {
      "default": "#dedcd3",
      "paper": "#dedcd3"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#fe3939"
    }
  },
  "typography": {
    "fontFamily": "'Montreal', sans-serif",
    "h1": {
      "fontSize": "38.4px",
      "fontWeight": "400",
      "lineHeight": "42.24px"
    },
    "h2": {
      "fontSize": "25px",
      "fontWeight": "400",
      "lineHeight": "35px"
    },
    "h3": {
      "fontSize": "20px",
      "fontWeight": "400",
      "lineHeight": "normal"
    },
    "body1": {
      "fontSize": "18px",
      "fontWeight": "400",
      "lineHeight": "25.2px"
    }
  },
  "shape": {
    "borderRadius": 3
  },
  "shadows": []
};

export default theme;
