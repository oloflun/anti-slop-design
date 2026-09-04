// React Theme — extracted from https://www.limon.no/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    accent: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '14': string;
    '16': string;
    '19': string;
    '20': string;
    '26': string;
    '30': string;
    '36': string;
    '46': string;
    '54': string;
    '68': string;
    '75': string;
 *   };
 *   space: {
    '0': string;
    '25': string;
    '30': string;
    '40': string;
    '45': string;
    '50': string;
    '60': string;
    '75': string;
    '80': string;
    '120': string;
    '144': string;
    '165': string;
    '320': string;
 *   };
 *   radii: {
    xs: string;
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
    "primary": "#f7ea48",
    "secondary": "#103b15",
    "accent": "#1d0b0d",
    "background": "#1d0b0d",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#fcf9f0",
    "neutral200": "#dbe2dc",
    "neutral300": "#ffffff"
  },
  "fonts": {
    "body": "'FreeSans', sans-serif"
  },
  "fontSizes": {
    "14": "14px",
    "16": "16px",
    "19": "19px",
    "20": "20px",
    "26": "26px",
    "30": "30px",
    "36": "36px",
    "46": "46px",
    "54": "54px",
    "68": "68px",
    "75": "75px"
  },
  "space": {
    "0": "0px",
    "25": "25px",
    "30": "30px",
    "40": "40px",
    "45": "45px",
    "50": "50px",
    "60": "60px",
    "75": "75px",
    "80": "80px",
    "120": "120px",
    "144": "144px",
    "165": "165px",
    "320": "320px"
  },
  "radii": {
    "xs": "1px",
    "full": "100px"
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
      "main": "#f7ea48",
      "light": "hsl(56, 92%, 78%)",
      "dark": "hsl(56, 92%, 48%)"
    },
    "secondary": {
      "main": "#103b15",
      "light": "hsl(127, 57%, 30%)",
      "dark": "hsl(127, 57%, 10%)"
    },
    "background": {
      "default": "#1d0b0d",
      "paper": "#fcf9f0"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#1d0b0d"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "36px",
      "fontWeight": "700",
      "lineHeight": "43.2px"
    },
    "h2": {
      "fontSize": "30px",
      "fontWeight": "400",
      "lineHeight": "40.5px"
    }
  },
  "shape": {
    "borderRadius": 1
  },
  "shadows": []
};

export default theme;
