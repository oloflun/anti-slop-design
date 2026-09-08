// React Theme — extracted from http://127.0.0.1:3055/sites/tidvatten.html
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
    neutral500: string;
    neutral600: string;
 *   };
 *   fonts: {
    body: string;
    mono: string;
 *   };
 *   fontSizes: {
    '64': string;
    '166.4': string;
    '147.2': string;
    '76.8': string;
    '46.08': string;
    '43.52': string;
    '35.84': string;
    '34.56': string;
    '30.72': string;
    '25.6': string;
    '23.04': string;
    '22.5': string;
 *   };
 *   space: {
    '5': string;
    '45': string;
    '63': string;
    '72': string;
    '90': string;
    '108': string;
    '162': string;
    '180': string;
    '198': string;
 *   };
 *   radii: {

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
    "primary": "#680c00",
    "secondary": "#af2c0a",
    "background": "#cbd6de",
    "foreground": "#020304",
    "neutral50": "#e5e7eb",
    "neutral100": "#020304",
    "neutral200": "#d6e0e5",
    "neutral300": "#12161b",
    "neutral400": "#6d7c85",
    "neutral500": "#cbd6de",
    "neutral600": "#b1c0ca"
  },
  "fonts": {
    "body": "'Familjen Grotesk', sans-serif",
    "mono": "'Fragment Mono', monospace"
  },
  "fontSizes": {
    "64": "64px",
    "166.4": "166.4px",
    "147.2": "147.2px",
    "76.8": "76.8px",
    "46.08": "46.08px",
    "43.52": "43.52px",
    "35.84": "35.84px",
    "34.56": "34.56px",
    "30.72": "30.72px",
    "25.6": "25.6px",
    "23.04": "23.04px",
    "22.5": "22.5px"
  },
  "space": {
    "5": "5px",
    "45": "45px",
    "63": "63px",
    "72": "72px",
    "90": "90px",
    "108": "108px",
    "162": "162px",
    "180": "180px",
    "198": "198px"
  },
  "radii": {},
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
      "main": "#680c00",
      "light": "hsl(7, 100%, 35%)",
      "dark": "hsl(7, 100%, 10%)"
    },
    "secondary": {
      "main": "#af2c0a",
      "light": "hsl(12, 89%, 51%)",
      "dark": "hsl(12, 89%, 21%)"
    },
    "background": {
      "default": "#cbd6de",
      "paper": "#010204"
    },
    "text": {
      "primary": "#020304",
      "secondary": "#d6e0e5"
    }
  },
  "typography": {
    "fontFamily": "'Literata', sans-serif",
    "h1": {
      "fontSize": "43.52px",
      "fontWeight": "600",
      "lineHeight": "41.344px"
    }
  },
  "shape": {},
  "shadows": []
};

export default theme;
