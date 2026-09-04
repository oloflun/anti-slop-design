// React Theme — extracted from https://redbrick.coffee/
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
    neutral300: string;
    neutral400: string;
 *   };
 *   fonts: {
    body: string;
    heading: string;
 *   };
 *   fontSizes: {
    '0': string;
    '10': string;
    '15': string;
    '20': string;
    '30': string;
    '35': string;
    '60': string;
    '100': string;
    '105': string;
    '150': string;
 *   };
 *   space: {
    '1': string;
    '45': string;
    '64': string;
    '105': string;
    '210': string;
    '420': string;
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
    "primary": "#e82c2a",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#212529",
    "neutral200": "#f2f2f2",
    "neutral300": "#ffffff",
    "neutral400": "#121212"
  },
  "fonts": {
    "body": "'GTStandard-M', sans-serif",
    "heading": "'Editorial Old', sans-serif"
  },
  "fontSizes": {
    "0": "0px",
    "10": "10px",
    "15": "15px",
    "20": "20px",
    "30": "30px",
    "35": "35px",
    "60": "60px",
    "100": "100px",
    "105": "105px",
    "150": "150px"
  },
  "space": {
    "1": "1px",
    "45": "45px",
    "64": "64px",
    "105": "105px",
    "210": "210px",
    "420": "420px"
  },
  "radii": {
    "sm": "4px",
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
      "main": "#e82c2a",
      "light": "hsl(1, 81%, 69%)",
      "dark": "hsl(1, 81%, 39%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#f2f2f2"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#212529"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "35px",
      "fontWeight": "400",
      "lineHeight": "52.5px",
      "fontFamily": "'Editorial Old', sans-serif"
    },
    "h2": {
      "fontSize": "30px",
      "fontWeight": "400",
      "lineHeight": "45px",
      "fontFamily": "'Editorial Old', sans-serif"
    }
  },
  "shape": {
    "borderRadius": 4
  },
  "shadows": []
};

export default theme;
